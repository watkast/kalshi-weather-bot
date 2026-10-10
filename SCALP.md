# Range-Scalp Bot

*Updated Sat Oct 10 23:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11023 | 9506 | 1517 (22) | 6 | $-3733.41 | -5.4% |
| **+10¢** | 8345 | 6577 | 1768 (36) | 6 | $-3568.30 | -6.8% |
| **+15¢** | 7037 | 5167 | 1870 (52) | 6 | $-3007.38 | -6.8% |
| **+20¢** | 6262 | 4315 | 1947 (66) | 6 | $-2541.56 | -6.5% |
| **+10¢ (15¢ stop)** | 13591 | 13550 | 41 (25) | 0 | $-5471.81 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 22:58 | +10 stop | NEAR | UP | 0.52 | 0.69 | 1.36 |
| 10-10 22:56 | +10 stop | XRP | DOWN | 0.56 | 0.33 | -2.62 |
| 10-10 22:56 | +10 stop | ZEC | UP | 0.54 | 0.39 | -1.85 |
| 10-10 22:56 | +15 | ZEC | UP | 0.53 | 0.70 | 1.37 |
| 10-10 22:56 | +10 | ZEC | UP | 0.53 | 0.65 | 0.86 |
| 10-10 22:56 | +5 | ZEC | UP | 0.53 | 0.65 | 0.86 |
| 10-10 22:56 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-10 22:56 | +10 stop | BNB | DOWN | 0.57 | 0.73 | 1.32 |
| 10-10 22:56 | +10 stop | ETH | UP | 0.71 | 0.55 | -1.93 |
| 10-10 22:55 | +10 stop | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 10-10 22:55 | +10 stop | HYPE | DOWN | 0.54 | 0.71 | 1.37 |
| 10-10 22:55 | +20 | HYPE | DOWN | 0.54 | 0.83 | 2.62 |
| 10-10 22:55 | +15 | HYPE | DOWN | 0.54 | 0.71 | 1.37 |
| 10-10 22:55 | +10 | HYPE | DOWN | 0.54 | 0.71 | 1.37 |
| 10-10 22:55 | +5 | HYPE | DOWN | 0.54 | 0.71 | 1.37 |
| 10-10 22:55 | +10 stop | SOL | UP | 0.57 | 0.77 | 1.69 |
| 10-10 22:54 | +10 stop | DOGE | DOWN | 0.67 | 0.47 | -2.34 |
| 10-10 22:54 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-10 22:54 | +15 | DOGE | DOWN | 0.66 | open |  |
| 10-10 22:54 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-10 22:54 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-10 22:54 | +10 stop | ZEC | UP | 0.60 | 0.75 | 1.19 |
| 10-10 22:54 | +20 | ZEC | UP | 0.60 | 0.81 | 1.82 |
| 10-10 22:54 | +15 | ZEC | UP | 0.60 | 0.75 | 1.19 |
| 10-10 22:54 | +10 | ZEC | UP | 0.60 | 0.75 | 1.19 |
| 10-10 22:54 | +5 | ZEC | UP | 0.60 | 0.75 | 1.19 |
| 10-10 22:53 | +10 stop | NEAR | DOWN | 0.55 | 0.32 | -2.64 |
| 10-10 22:53 | +20 | NEAR | DOWN | 0.55 | 0.78 | 1.99 |
| 10-10 22:53 | +15 | NEAR | DOWN | 0.55 | 0.78 | 1.99 |
| 10-10 22:53 | +10 | NEAR | DOWN | 0.55 | 0.68 | 0.96 |
| 10-10 22:53 | +5 | NEAR | DOWN | 0.55 | 0.68 | 0.96 |
| 10-10 22:53 | +10 stop | BNB | DOWN | 0.68 | 0.51 | -2.05 |
| 10-10 22:53 | +20 | BNB | DOWN | 0.70 | open |  |
| 10-10 22:53 | +15 | BNB | DOWN | 0.68 | open |  |
| 10-10 22:53 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-10 22:53 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-10 22:53 | +10 stop | SOL | DOWN | 0.63 | 0.45 | -2.15 |
| 10-10 22:53 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-10 22:53 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-10 22:53 | +10 | SOL | DOWN | 0.63 | open |  |
