# Range-Scalp Bot

*Updated Sat Nov 14 05:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59053 | 51521 | 7532 (106) | 0 | $-15979.65 | -4.3% |
| **+10¢** | 44124 | 35318 | 8806 (139) | 0 | $-14947.72 | -5.4% |
| **+15¢** | 36973 | 27480 | 9493 (174) | 0 | $-13571.27 | -5.9% |
| **+20¢** | 32940 | 22972 | 9968 (226) | 0 | $-11967.30 | -5.8% |
| **+10¢ (15¢ stop)** | 71890 | 71752 | 138 (82) | 0 | $-26422.04 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 04:58 | +10 | BNB | UP | 0.68 | no | -6.96 |
| 11-14 04:57 | +10 stop | SOL | UP | 0.65 | 0.79 | 1.12 |
| 11-14 04:57 | +10 | SOL | UP | 0.65 | 0.79 | 1.12 |
| 11-14 04:57 | +20 | SOL | UP | 0.68 | no | -6.96 |
| 11-14 04:57 | +10 stop | NEAR | DOWN | 0.71 | 0.94 | 2.05 |
| 11-14 04:57 | +10 stop | BNB | UP | 0.50 | 0.72 | 1.85 |
| 11-14 04:57 | +10 | BNB | UP | 0.47 | 0.57 | 0.64 |
| 11-14 04:57 | +5 | BNB | UP | 0.48 | 0.57 | 0.54 |
| 11-14 04:56 | +10 stop | ETH | UP | 0.51 | 0.65 | 1.06 |
| 11-14 04:55 | +10 stop | NEAR | UP | 0.59 | 0.43 | -1.95 |
| 11-14 04:55 | +10 | NEAR | UP | 0.59 | no | -6.07 |
| 11-14 04:55 | +5 | NEAR | UP | 0.59 | no | -6.07 |
| 11-14 04:55 | +5 | SOL | DOWN | 0.60 | 0.77 | 1.40 |
| 11-14 04:55 | +10 stop | SOL | UP | 0.47 | 0.57 | 0.64 |
| 11-14 04:55 | +15 | SOL | UP | 0.47 | 0.62 | 1.15 |
| 11-14 04:55 | +10 | SOL | UP | 0.47 | 0.57 | 0.64 |
| 11-14 04:55 | +5 | SOL | UP | 0.47 | 0.56 | 0.54 |
| 11-14 04:54 | +10 stop | BTC | UP | 0.53 | 0.70 | 1.37 |
| 11-14 04:54 | +10 stop | BNB | UP | 0.67 | 0.77 | 0.71 |
| 11-14 04:54 | +20 | SOL | DOWN | 0.41 | 0.61 | 1.66 |
| 11-14 04:54 | +15 | SOL | DOWN | 0.40 | 0.57 | 1.35 |
| 11-14 04:54 | +10 | SOL | DOWN | 0.41 | 0.57 | 1.25 |
| 11-14 04:54 | +5 | SOL | DOWN | 0.41 | 0.57 | 1.25 |
| 11-14 04:53 | +10 stop | ETH | DOWN | 0.62 | 0.45 | -2.05 |
| 11-14 04:53 | +10 stop | HYPE | UP | 0.68 | 0.83 | 1.24 |
| 11-14 04:53 | +5 | HYPE | UP | 0.68 | 0.75 | 0.40 |
| 11-14 04:52 | +10 stop | XRP | UP | 0.52 | 0.66 | 1.06 |
| 11-14 04:52 | +10 stop | DOGE | DOWN | 0.58 | 0.40 | -2.15 |
| 11-14 04:52 | +10 stop | NEAR | DOWN | 0.68 | 0.51 | -2.04 |
| 11-14 04:52 | +10 stop | BTC | DOWN | 0.70 | 0.48 | -2.53 |
| 11-14 04:52 | +10 stop | SOL | DOWN | 0.69 | 0.48 | -2.43 |
| 11-14 04:52 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 11-14 04:52 | +10 stop | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 11-14 04:51 | +5 | DOGE | UP | 0.53 | 0.59 | 0.25 |
| 11-14 04:51 | +10 stop | BTC | UP | 0.61 | 0.43 | -2.15 |
| 11-14 04:50 | +5 | HYPE | UP | 0.52 | 0.61 | 0.55 |
| 11-14 04:50 | +5 | DOGE | UP | 0.63 | 0.69 | 0.30 |
| 11-14 04:50 | +10 stop | SOL | UP | 0.62 | 0.39 | -2.61 |
| 11-14 04:49 | +10 stop | BTC | UP | 0.71 | 0.52 | -2.23 |
| 11-14 04:49 | +10 | BTC | UP | 0.71 | 0.82 | 0.84 |
