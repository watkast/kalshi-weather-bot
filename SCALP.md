# Range-Scalp Bot

*Updated Thu Nov 05 05:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48085 | 41876 | 6209 (73) | 1 | $-13840.33 | -4.6% |
| **+10¢** | 35921 | 28708 | 7213 (99) | 2 | $-12703.24 | -5.6% |
| **+15¢** | 30101 | 22336 | 7765 (127) | 2 | $-11605.80 | -6.1% |
| **+20¢** | 26741 | 18607 | 8134 (166) | 2 | $-10264.94 | -6.1% |
| **+10¢ (15¢ stop)** | 58607 | 58514 | 93 (56) | 0 | $-21769.35 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 05:25 | +10 stop | XRP | DOWN | 0.61 | 0.43 | -2.15 |
| 11-05 05:25 | +20 | XRP | DOWN | 0.60 | open |  |
| 11-05 05:25 | +15 | XRP | DOWN | 0.60 | open |  |
| 11-05 05:25 | +10 | XRP | DOWN | 0.60 | open |  |
| 11-05 05:25 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 11-05 05:21 | +10 stop | XRP | DOWN | 0.65 | 0.43 | -2.54 |
| 11-05 05:21 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 11-05 05:21 | +10 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 11-05 05:20 | +5 | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 11-05 05:18 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-05 05:18 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 11-05 05:17 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 11-05 05:17 | +10 stop | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-05 05:17 | +20 | ETH | DOWN | 0.65 | 0.87 | 1.96 |
| 11-05 05:17 | +15 | ETH | DOWN | 0.65 | 0.80 | 1.22 |
| 11-05 05:17 | +10 | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-05 05:17 | +5 | ETH | DOWN | 0.65 | 0.72 | 0.39 |
| 11-05 05:17 | +10 stop | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 11-05 05:17 | +20 | XRP | DOWN | 0.58 | 0.82 | 2.11 |
| 11-05 05:17 | +15 | XRP | DOWN | 0.58 | 0.73 | 1.18 |
| 11-05 05:17 | +10 | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 11-05 05:17 | +5 | XRP | DOWN | 0.58 | 0.65 | 0.36 |
| 11-05 05:17 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.01 |
| 11-05 05:17 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 11-05 05:17 | +15 | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 11-05 05:17 | +10 | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 11-05 05:17 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 11-05 05:17 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-05 05:17 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-05 05:17 | +15 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-05 05:17 | +10 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-05 05:17 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-05 05:17 | +10 stop | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-05 05:17 | +20 | NEAR | DOWN | 0.69 | 0.90 | 1.88 |
| 11-05 05:17 | +15 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-05 05:17 | +10 | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-05 05:17 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 11-05 05:17 | +10 stop | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-05 05:17 | +20 | BTC | DOWN | 0.64 | 0.89 | 2.26 |
| 11-05 05:17 | +15 | BTC | DOWN | 0.64 | 0.80 | 1.31 |
