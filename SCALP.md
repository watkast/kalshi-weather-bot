# Range-Scalp Bot

*Updated Sat Oct 31 02:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41674 | 36365 | 5309 (54) | 4 | $-11687.76 | -4.5% |
| **+10¢** | 31061 | 24917 | 6144 (78) | 4 | $-10432.67 | -5.3% |
| **+15¢** | 25959 | 19335 | 6624 (106) | 4 | $-9524.17 | -5.8% |
| **+20¢** | 23043 | 16104 | 6939 (137) | 5 | $-8411.87 | -5.8% |
| **+10¢ (15¢ stop)** | 50797 | 50722 | 75 (41) | 0 | $-19188.15 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 02:54 | +10 stop | NEAR | DOWN | 0.61 | 0.92 | 2.83 |
| 10-31 02:54 | +10 stop | SOL | DOWN | 0.62 | 0.81 | 1.62 |
| 10-31 02:53 | +10 stop | ETH | UP | 0.57 | 0.70 | 0.97 |
| 10-31 02:52 | +10 stop | NEAR | UP | 0.57 | 0.41 | -1.95 |
| 10-31 02:52 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-31 02:52 | +10 stop | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
| 10-31 02:49 | +10 stop | NEAR | DOWN | 0.63 | 0.48 | -1.85 |
| 10-31 02:49 | +10 stop | ETH | DOWN | 0.53 | 0.38 | -1.85 |
| 10-31 02:49 | +10 stop | ZEC | DOWN | 0.63 | 0.81 | 1.52 |
| 10-31 02:49 | +10 stop | HYPE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-31 02:49 | +20 | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
| 10-31 02:49 | +15 | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-31 02:49 | +10 | HYPE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-31 02:48 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-31 02:48 | +5 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-31 02:47 | +10 stop | SOL | DOWN | 0.55 | 0.66 | 0.77 |
| 10-31 02:47 | +10 stop | DOGE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-31 02:47 | +10 stop | BTC | DOWN | 0.56 | 0.75 | 1.58 |
| 10-31 02:47 | +20 | BTC | DOWN | 0.56 | open |  |
| 10-31 02:47 | +15 | BTC | DOWN | 0.56 | 0.75 | 1.58 |
| 10-31 02:47 | +10 | BTC | DOWN | 0.56 | 0.75 | 1.58 |
| 10-31 02:47 | +5 | BTC | DOWN | 0.56 | 0.62 | 0.25 |
| 10-31 02:46 | +10 stop | ZEC | UP | 0.57 | 0.40 | -2.05 |
| 10-31 02:46 | +20 | ZEC | UP | 0.57 | open |  |
| 10-31 02:46 | +15 | ZEC | UP | 0.57 | open |  |
| 10-31 02:46 | +10 | ZEC | UP | 0.56 | open |  |
| 10-31 02:46 | +5 | ZEC | UP | 0.56 | open |  |
| 10-31 02:46 | +10 stop | BNB | UP | 0.67 | 0.80 | 1.02 |
| 10-31 02:46 | +20 | BNB | UP | 0.67 | 0.87 | 1.76 |
| 10-31 02:46 | +15 | BNB | UP | 0.67 | 0.82 | 1.23 |
| 10-31 02:46 | +10 | BNB | UP | 0.67 | 0.80 | 1.02 |
| 10-31 02:46 | +5 | BNB | UP | 0.67 | 0.75 | 0.50 |
| 10-31 02:46 | +10 stop | DOGE | UP | 0.57 | 0.39 | -2.15 |
| 10-31 02:46 | +20 | DOGE | UP | 0.57 | open |  |
| 10-31 02:46 | +15 | DOGE | UP | 0.57 | open |  |
| 10-31 02:46 | +10 | DOGE | UP | 0.57 | open |  |
| 10-31 02:46 | +5 | DOGE | UP | 0.57 | open |  |
| 10-31 02:46 | +10 stop | HYPE | DOWN | 0.49 | 0.68 | 1.56 |
| 10-31 02:46 | +20 | HYPE | DOWN | 0.49 | 0.72 | 1.97 |
| 10-31 02:46 | +15 | HYPE | DOWN | 0.49 | 0.68 | 1.56 |
