# Range-Scalp Bot

*Updated Thu Oct 08 22:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8103 | 7016 | 1087 (13) | 7 | $-2593.17 | -5.1% |
| **+10¢** | 6134 | 4847 | 1287 (25) | 7 | $-2558.53 | -6.6% |
| **+15¢** | 5162 | 3809 | 1353 (37) | 8 | $-2066.54 | -6.4% |
| **+20¢** | 4608 | 3205 | 1403 (45) | 8 | $-1644.42 | -5.7% |
| **+10¢ (15¢ stop)** | 9844 | 9814 | 30 (19) | 0 | $-3620.71 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 22:38 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 10-08 22:38 | +10 stop | BNB | UP | 0.54 | 0.68 | 1.06 |
| 10-08 22:37 | +10 stop | ETH | UP | 0.63 | 0.77 | 1.10 |
| 10-08 22:37 | +10 stop | ETH | DOWN | 0.46 | 0.61 | 1.15 |
| 10-08 22:36 | +10 stop | BNB | UP | 0.51 | 0.63 | 0.85 |
| 10-08 22:36 | +10 stop | ETH | UP | 0.61 | 0.40 | -2.44 |
| 10-08 22:36 | +10 | ETH | UP | 0.61 | 0.77 | 1.30 |
| 10-08 22:36 | +5 | ETH | UP | 0.61 | 0.69 | 0.48 |
| 10-08 22:34 | +10 stop | ETH | UP | 0.57 | 0.69 | 0.87 |
| 10-08 22:34 | +10 | ETH | UP | 0.57 | 0.69 | 0.87 |
| 10-08 22:34 | +5 | ETH | UP | 0.57 | 0.69 | 0.87 |
| 10-08 22:34 | +10 stop | ETH | DOWN | 0.53 | 0.66 | 0.96 |
| 10-08 22:34 | +10 | ETH | DOWN | 0.53 | 0.66 | 0.96 |
| 10-08 22:34 | +5 | ETH | DOWN | 0.53 | 0.66 | 0.96 |
| 10-08 22:33 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 10-08 22:33 | +10 stop | BTC | UP | 0.70 | 0.81 | 0.84 |
| 10-08 22:33 | +10 stop | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 10-08 22:33 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-08 22:33 | +20 | ZEC | UP | 0.68 | 0.88 | 1.76 |
| 10-08 22:33 | +15 | ZEC | UP | 0.68 | 0.86 | 1.55 |
| 10-08 22:33 | +10 | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-08 22:33 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 10-08 22:33 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-08 22:32 | +10 stop | NEAR | DOWN | 0.66 | 0.47 | -2.24 |
| 10-08 22:32 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-08 22:32 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-08 22:32 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-08 22:32 | +5 | NEAR | DOWN | 0.66 | open |  |
| 10-08 22:31 | +10 stop | SOL | DOWN | 0.68 | 0.52 | -1.94 |
| 10-08 22:31 | +20 | SOL | DOWN | 0.68 | open |  |
| 10-08 22:31 | +15 | SOL | DOWN | 0.68 | open |  |
| 10-08 22:31 | +10 | SOL | DOWN | 0.68 | open |  |
| 10-08 22:31 | +5 | SOL | DOWN | 0.68 | open |  |
| 10-08 22:31 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-08 22:31 | +20 | ETH | DOWN | 0.65 | open |  |
| 10-08 22:31 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-08 22:31 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-08 22:31 | +5 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-08 22:31 | +10 stop | BNB | DOWN | 0.69 | 0.50 | -2.27 |
| 10-08 22:31 | +20 | BNB | DOWN | 0.69 | open |  |
