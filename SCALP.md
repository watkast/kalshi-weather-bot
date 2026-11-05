# Range-Scalp Bot

*Updated Thu Nov 05 14:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48449 | 42213 | 6236 (73) | 0 | $-13803.19 | -4.5% |
| **+10¢** | 36168 | 28925 | 7243 (99) | 0 | $-12638.19 | -5.6% |
| **+15¢** | 30303 | 22502 | 7801 (127) | 1 | $-11540.04 | -6.1% |
| **+20¢** | 26922 | 18749 | 8173 (166) | 1 | $-10194.09 | -6.0% |
| **+10¢ (15¢ stop)** | 59054 | 58961 | 93 (56) | 0 | $-21925.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 14:54 | +5 | BNB | DOWN | 0.58 | 0.65 | 0.36 |
| 11-05 14:54 | +10 stop | BNB | DOWN | 0.56 | 0.79 | 2.01 |
| 11-05 14:54 | +20 | BNB | DOWN | 0.56 | 0.79 | 2.01 |
| 11-05 14:54 | +15 | BNB | DOWN | 0.56 | 0.79 | 2.00 |
| 11-05 14:54 | +10 | BNB | DOWN | 0.56 | 0.79 | 2.00 |
| 11-05 14:54 | +5 | BNB | DOWN | 0.56 | 0.61 | 0.15 |
| 11-05 14:52 | +10 stop | HYPE | DOWN | 0.62 | 0.81 | 1.62 |
| 11-05 14:51 | +5 | XRP | DOWN | 0.70 | 0.83 | 1.00 |
| 11-05 14:51 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 11-05 14:49 | +10 stop | HYPE | UP | 0.55 | 0.66 | 0.76 |
| 11-05 14:49 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.70 |
| 11-05 14:48 | +15 | NEAR | DOWN | 0.63 | 0.81 | 1.52 |
| 11-05 14:48 | +5 | NEAR | DOWN | 0.63 | 0.81 | 1.52 |
| 11-05 14:48 | +10 stop | BNB | DOWN | 0.69 | 0.88 | 1.67 |
| 11-05 14:48 | +15 | BNB | DOWN | 0.69 | 0.88 | 1.67 |
| 11-05 14:48 | +10 | BNB | DOWN | 0.70 | 0.88 | 1.57 |
| 11-05 14:48 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-05 14:48 | +10 stop | DOGE | DOWN | 0.71 | 0.56 | -1.83 |
| 11-05 14:48 | +10 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-05 14:48 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-05 14:48 | +10 stop | NEAR | DOWN | 0.70 | 0.54 | -1.93 |
| 11-05 14:48 | +10 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-05 14:47 | +15 | HYPE | DOWN | 0.69 | 0.88 | 1.67 |
| 11-05 14:47 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-05 14:47 | +5 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-05 14:47 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-05 14:47 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-05 14:47 | +10 stop | HYPE | DOWN | 0.68 | 0.51 | -2.04 |
| 11-05 14:47 | +5 | NEAR | DOWN | 0.65 | 0.73 | 0.50 |
| 11-05 14:47 | +5 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-05 14:47 | +10 stop | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-05 14:47 | +10 | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-05 14:47 | +5 | XRP | DOWN | 0.58 | 0.64 | 0.25 |
| 11-05 14:47 | +10 stop | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-05 14:47 | +20 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 11-05 14:47 | +15 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-05 14:47 | +10 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-05 14:47 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 11-05 14:47 | +10 stop | XRP | UP | 0.50 | 0.60 | 0.65 |
| 11-05 14:47 | +20 | XRP | UP | 0.50 | open |  |
