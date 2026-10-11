# Range-Scalp Bot

*Updated Sun Oct 11 16:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12189 | 10513 | 1676 (24) | 1 | $-4075.04 | -5.3% |
| **+10¢** | 9262 | 7318 | 1944 (37) | 1 | $-3844.66 | -6.6% |
| **+15¢** | 7804 | 5741 | 2063 (54) | 3 | $-3282.15 | -6.7% |
| **+20¢** | 6952 | 4803 | 2149 (68) | 4 | $-2781.78 | -6.4% |
| **+10¢ (15¢ stop)** | 15017 | 14976 | 41 (25) | 0 | $-5920.62 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 16:42 | +10 stop | ETH | DOWN | 0.41 | 0.65 | 2.07 |
| 10-11 16:42 | +20 | ETH | DOWN | 0.42 | 0.65 | 1.96 |
| 10-11 16:42 | +15 | ETH | DOWN | 0.42 | 0.65 | 1.96 |
| 10-11 16:42 | +10 | ETH | DOWN | 0.42 | 0.65 | 1.96 |
| 10-11 16:42 | +5 | ETH | DOWN | 0.44 | 0.65 | 1.76 |
| 10-11 16:41 | +10 stop | ZEC | UP | 0.50 | 0.84 | 3.12 |
| 10-11 16:40 | +10 stop | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 10-11 16:40 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-11 16:40 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-11 16:40 | +10 | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 10-11 16:40 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 10-11 16:39 | +10 stop | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 10-11 16:39 | +15 | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 10-11 16:39 | +10 | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 10-11 16:39 | +5 | XRP | DOWN | 0.58 | 0.65 | 0.36 |
| 10-11 16:38 | +10 stop | BNB | UP | 0.67 | 0.78 | 0.77 |
| 10-11 16:38 | +5 | BNB | UP | 0.67 | 0.74 | 0.36 |
| 10-11 16:38 | +10 stop | DOGE | UP | 0.66 | 0.82 | 1.33 |
| 10-11 16:38 | +10 stop | ZEC | UP | 0.68 | 0.50 | -2.14 |
| 10-11 16:38 | +10 | ZEC | UP | 0.68 | 0.84 | 1.34 |
| 10-11 16:38 | +5 | ZEC | UP | 0.68 | 0.84 | 1.34 |
| 10-11 16:38 | +10 stop | DOGE | DOWN | 0.59 | 0.44 | -1.85 |
| 10-11 16:37 | +10 stop | BNB | DOWN | 0.65 | 0.34 | -3.42 |
| 10-11 16:37 | +10 stop | ZEC | DOWN | 0.47 | 0.59 | 0.85 |
| 10-11 16:37 | +10 | ZEC | DOWN | 0.46 | 0.59 | 0.95 |
| 10-11 16:37 | +5 | ZEC | DOWN | 0.46 | 0.59 | 0.95 |
| 10-11 16:36 | +10 stop | DOGE | DOWN | 0.71 | 0.55 | -1.93 |
| 10-11 16:36 | +10 | DOGE | DOWN | 0.70 | open |  |
| 10-11 16:36 | +5 | DOGE | DOWN | 0.70 | open |  |
| 10-11 16:34 | +15 | HYPE | UP | 0.67 | 0.89 | 1.97 |
| 10-11 16:34 | +5 | HYPE | UP | 0.67 | 0.72 | 0.19 |
| 10-11 16:34 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.70 |
| 10-11 16:34 | +10 | ZEC | DOWN | 0.63 | 0.73 | 0.70 |
| 10-11 16:34 | +5 | ZEC | DOWN | 0.65 | 0.73 | 0.53 |
| 10-11 16:34 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 10-11 16:34 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 10-11 16:33 | +5 | NEAR | UP | 0.69 | 0.77 | 0.52 |
| 10-11 16:33 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-11 16:33 | +10 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-11 16:32 | +5 | HYPE | UP | 0.67 | 0.73 | 0.26 |
