# Range-Scalp Bot

*Updated Fri Oct 09 09:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8880 | 7680 | 1200 (13) | 5 | $-2921.90 | -5.2% |
| **+10¢** | 6722 | 5313 | 1409 (25) | 5 | $-2813.46 | -6.6% |
| **+15¢** | 5672 | 4188 | 1484 (37) | 4 | $-2287.19 | -6.4% |
| **+20¢** | 5047 | 3506 | 1541 (45) | 4 | $-1892.45 | -6.0% |
| **+10¢ (15¢ stop)** | 10829 | 10799 | 30 (19) | 1 | $-4059.48 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 09:42 | +10 stop | BNB | DOWN | 0.62 | open |  |
| 10-09 09:42 | +5 | BNB | DOWN | 0.62 | open |  |
| 10-09 09:41 | +10 stop | BNB | DOWN | 0.41 | 0.56 | 1.15 |
| 10-09 09:41 | +5 | BNB | DOWN | 0.41 | 0.56 | 1.15 |
| 10-09 09:40 | +10 stop | BNB | UP | 0.48 | 0.61 | 0.95 |
| 10-09 09:40 | +15 | BNB | UP | 0.48 | open |  |
| 10-09 09:40 | +5 | BNB | UP | 0.48 | 0.61 | 0.95 |
| 10-09 09:39 | +10 stop | NEAR | UP | 0.67 | 0.79 | 0.92 |
| 10-09 09:39 | +5 | NEAR | UP | 0.67 | 0.72 | 0.19 |
| 10-09 09:39 | +10 stop | DOGE | DOWN | 0.60 | 0.40 | -2.34 |
| 10-09 09:38 | +10 stop | HYPE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-09 09:38 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-09 09:38 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-09 09:38 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-09 09:37 | +10 stop | DOGE | UP | 0.67 | 0.46 | -2.44 |
| 10-09 09:37 | +5 | NEAR | UP | 0.62 | 0.70 | 0.48 |
| 10-09 09:36 | +5 | SOL | UP | 0.67 | open |  |
| 10-09 09:36 | +5 | DOGE | DOWN | 0.57 | open |  |
| 10-09 09:36 | +10 stop | DOGE | DOWN | 0.58 | 0.28 | -3.32 |
| 10-09 09:36 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 10-09 09:35 | +5 | NEAR | UP | 0.54 | 0.59 | 0.15 |
| 10-09 09:35 | +10 stop | SOL | UP | 0.57 | 0.37 | -2.35 |
| 10-09 09:35 | +5 | SOL | UP | 0.56 | 0.62 | 0.21 |
| 10-09 09:35 | +10 stop | NEAR | UP | 0.63 | 0.79 | 1.31 |
| 10-09 09:35 | +5 | NEAR | UP | 0.64 | 0.69 | 0.18 |
| 10-09 09:35 | +10 stop | XRP | DOWN | 0.66 | 0.79 | 1.02 |
| 10-09 09:35 | +15 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 10-09 09:35 | +10 | XRP | DOWN | 0.66 | 0.79 | 1.02 |
| 10-09 09:35 | +5 | XRP | DOWN | 0.65 | 0.73 | 0.49 |
| 10-09 09:35 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-09 09:35 | +15 | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 10-09 09:35 | +10 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-09 09:35 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-09 09:35 | +10 stop | ETH | UP | 0.60 | 0.34 | -2.93 |
| 10-09 09:35 | +10 | ETH | UP | 0.60 | open |  |
| 10-09 09:35 | +5 | ETH | UP | 0.60 | open |  |
| 10-09 09:35 | +10 stop | BNB | UP | 0.60 | 0.32 | -3.13 |
| 10-09 09:34 | +5 | DOGE | DOWN | 0.53 | 0.58 | 0.14 |
| 10-09 09:34 | +5 | SOL | DOWN | 0.52 | 0.59 | 0.35 |
| 10-09 09:34 | +10 stop | BNB | DOWN | 0.62 | 0.41 | -2.43 |
