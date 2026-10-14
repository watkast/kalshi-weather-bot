# Range-Scalp Bot

*Updated Wed Oct 14 15:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16143 | 13984 | 2159 (27) | 0 | $-5112.75 | -5.0% |
| **+10¢** | 12201 | 9701 | 2500 (39) | 0 | $-4710.83 | -6.1% |
| **+15¢** | 10260 | 7574 | 2686 (58) | 0 | $-4227.07 | -6.6% |
| **+20¢** | 9128 | 6311 | 2817 (75) | 0 | $-3737.77 | -6.5% |
| **+10¢ (15¢ stop)** | 19876 | 19826 | 50 (29) | 0 | $-7635.39 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 15:07 | +10 stop | XRP | DOWN | 0.70 | 0.88 | 1.57 |
| 10-14 15:06 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-14 15:05 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 10-14 15:05 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-14 15:05 | +5 | DOGE | DOWN | 0.62 | 0.70 | 0.48 |
| 10-14 15:05 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 10-14 15:04 | +10 stop | XRP | UP | 0.50 | 0.34 | -1.94 |
| 10-14 15:04 | +10 stop | ETH | UP | 0.61 | 0.37 | -2.74 |
| 10-14 15:04 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-14 15:04 | +15 | ZEC | DOWN | 0.70 | 0.86 | 1.33 |
| 10-14 15:04 | +10 | ZEC | DOWN | 0.70 | 0.84 | 1.12 |
| 10-14 15:04 | +5 | ZEC | DOWN | 0.70 | 0.80 | 0.71 |
| 10-14 15:04 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 10-14 15:04 | +10 stop | SOL | DOWN | 0.59 | 0.77 | 1.50 |
| 10-14 15:04 | +10 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-14 15:04 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 10-14 15:04 | +5 | DOGE | DOWN | 0.58 | 0.66 | 0.46 |
| 10-14 15:04 | +10 stop | HYPE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-14 15:02 | +10 stop | XRP | DOWN | 0.58 | 0.43 | -1.86 |
| 10-14 15:02 | +10 stop | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 10-14 15:02 | +10 stop | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 10-14 15:01 | +10 stop | HYPE | DOWN | 0.68 | 0.52 | -1.94 |
| 10-14 15:01 | +20 | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
| 10-14 15:01 | +15 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-14 15:01 | +10 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-14 15:01 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-14 15:01 | +10 stop | ETH | DOWN | 0.63 | 0.48 | -1.85 |
| 10-14 15:01 | +20 | ETH | DOWN | 0.63 | 0.89 | 2.36 |
| 10-14 15:01 | +15 | ETH | DOWN | 0.63 | 0.89 | 2.36 |
| 10-14 15:01 | +10 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-14 15:01 | +5 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-14 15:01 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-14 15:01 | +20 | DOGE | DOWN | 0.65 | 0.92 | 2.52 |
| 10-14 15:01 | +15 | DOGE | DOWN | 0.65 | 0.83 | 1.54 |
| 10-14 15:01 | +10 | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-14 15:01 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-14 15:01 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-14 15:01 | +20 | SOL | DOWN | 0.65 | 0.88 | 2.06 |
| 10-14 15:01 | +15 | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 10-14 15:01 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
