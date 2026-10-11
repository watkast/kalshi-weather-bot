# Range-Scalp Bot

*Updated Sun Oct 11 13:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12003 | 10358 | 1645 (24) | 2 | $-3995.21 | -5.3% |
| **+10¢** | 9107 | 7195 | 1912 (37) | 3 | $-3791.92 | -6.6% |
| **+15¢** | 7670 | 5640 | 2030 (54) | 4 | $-3244.15 | -6.7% |
| **+20¢** | 6837 | 4725 | 2112 (67) | 4 | $-2726.71 | -6.4% |
| **+10¢ (15¢ stop)** | 14777 | 14736 | 41 (25) | 0 | $-5853.63 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 13:43 | +10 stop | SOL | DOWN | 0.57 | 0.68 | 0.76 |
| 10-11 13:43 | +20 | SOL | DOWN | 0.57 | open |  |
| 10-11 13:43 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-11 13:43 | +10 | SOL | DOWN | 0.57 | 0.68 | 0.76 |
| 10-11 13:43 | +5 | SOL | DOWN | 0.57 | 0.68 | 0.76 |
| 10-11 13:43 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-11 13:42 | +10 stop | BNB | UP | 0.69 | 0.35 | -3.71 |
| 10-11 13:42 | +20 | BNB | UP | 0.69 | open |  |
| 10-11 13:42 | +15 | BNB | UP | 0.69 | open |  |
| 10-11 13:42 | +10 | BNB | UP | 0.69 | open |  |
| 10-11 13:42 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 10-11 13:42 | +10 stop | ETH | DOWN | 0.58 | 0.94 | 3.38 |
| 10-11 13:40 | +10 stop | HYPE | DOWN | 0.50 | 0.30 | -2.33 |
| 10-11 13:40 | +10 stop | ETH | UP | 0.61 | 0.44 | -2.05 |
| 10-11 13:40 | +10 | ETH | UP | 0.59 | open |  |
| 10-11 13:40 | +5 | ETH | UP | 0.59 | open |  |
| 10-11 13:37 | +10 stop | XRP | UP | 0.56 | 0.82 | 2.28 |
| 10-11 13:37 | +10 stop | HYPE | DOWN | 0.54 | 0.37 | -2.05 |
| 10-11 13:36 | +10 stop | XRP | DOWN | 0.59 | 0.42 | -2.05 |
| 10-11 13:36 | +10 stop | BTC | DOWN | 0.49 | 0.16 | -3.58 |
| 10-11 13:35 | +10 stop | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 10-11 13:35 | +20 | DOGE | UP | 0.66 | 0.86 | 1.80 |
| 10-11 13:35 | +15 | DOGE | UP | 0.65 | 0.85 | 1.72 |
| 10-11 13:35 | +10 | DOGE | UP | 0.65 | 0.79 | 1.09 |
| 10-11 13:35 | +5 | DOGE | UP | 0.65 | 0.79 | 1.11 |
| 10-11 13:35 | +10 stop | ETH | DOWN | 0.66 | 0.37 | -3.23 |
| 10-11 13:35 | +10 stop | SOL | DOWN | 0.66 | 0.51 | -1.84 |
| 10-11 13:35 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 10-11 13:34 | +5 | BNB | UP | 0.62 | 0.69 | 0.38 |
| 10-11 13:34 | +10 stop | XRP | UP | 0.63 | 0.42 | -2.45 |
| 10-11 13:34 | +10 | XRP | UP | 0.63 | 0.82 | 1.62 |
| 10-11 13:34 | +5 | XRP | UP | 0.63 | 0.82 | 1.62 |
| 10-11 13:34 | +10 stop | SOL | UP | 0.68 | 0.38 | -3.33 |
| 10-11 13:33 | +5 | HYPE | UP | 0.70 | open |  |
| 10-11 13:33 | +5 | BNB | UP | 0.65 | 0.71 | 0.29 |
| 10-11 13:33 | +10 stop | ZEC | UP | 0.65 | 0.83 | 1.56 |
| 10-11 13:33 | +10 stop | SOL | UP | 0.67 | 0.52 | -1.84 |
| 10-11 13:31 | +10 stop | XRP | UP | 0.64 | 0.76 | 0.90 |
| 10-11 13:31 | +20 | XRP | UP | 0.64 | 0.84 | 1.73 |
| 10-11 13:31 | +15 | XRP | UP | 0.64 | 0.82 | 1.52 |
