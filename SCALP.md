# Range-Scalp Bot

*Updated Sun Oct 25 00:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32286 | 28153 | 4133 (41) | 4 | $-9192.30 | -4.5% |
| **+10¢** | 24172 | 19383 | 4789 (59) | 3 | $-8241.57 | -5.4% |
| **+15¢** | 20241 | 15091 | 5150 (82) | 4 | $-7372.60 | -5.8% |
| **+20¢** | 17931 | 12543 | 5388 (104) | 4 | $-6509.32 | -5.8% |
| **+10¢ (15¢ stop)** | 39684 | 39624 | 60 (32) | 2 | $-15179.97 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 00:42 | +10 stop | SOL | DOWN | 0.71 | open |  |
| 10-25 00:42 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-25 00:42 | +10 stop | HYPE | UP | 0.53 | open |  |
| 10-25 00:42 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-25 00:42 | +15 | SOL | DOWN | 0.70 | open |  |
| 10-25 00:42 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-25 00:41 | +10 stop | HYPE | DOWN | 0.70 | 0.41 | -3.22 |
| 10-25 00:41 | +10 | HYPE | DOWN | 0.70 | open |  |
| 10-25 00:41 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-25 00:41 | +10 stop | ZEC | DOWN | 0.52 | 0.72 | 1.67 |
| 10-25 00:40 | +10 stop | BTC | UP | 0.56 | 0.70 | 1.07 |
| 10-25 00:40 | +20 | BTC | UP | 0.56 | 0.76 | 1.69 |
| 10-25 00:40 | +15 | BTC | UP | 0.56 | 0.74 | 1.48 |
| 10-25 00:40 | +10 | BTC | UP | 0.56 | 0.70 | 1.07 |
| 10-25 00:40 | +5 | BTC | UP | 0.56 | 0.64 | 0.45 |
| 10-25 00:38 | +10 stop | SOL | UP | 0.61 | 0.45 | -1.95 |
| 10-25 00:38 | +10 stop | SOL | DOWN | 0.48 | 0.66 | 1.46 |
| 10-25 00:37 | +10 stop | ZEC | DOWN | 0.60 | 0.73 | 0.99 |
| 10-25 00:36 | +10 stop | HYPE | UP | 0.59 | 0.43 | -1.95 |
| 10-25 00:36 | +10 stop | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-25 00:36 | +10 stop | ZEC | DOWN | 0.58 | 0.69 | 0.77 |
| 10-25 00:35 | +10 stop | BTC | UP | 0.53 | 0.68 | 1.16 |
| 10-25 00:35 | +15 | BTC | UP | 0.53 | 0.68 | 1.16 |
| 10-25 00:35 | +10 | BTC | UP | 0.53 | 0.68 | 1.16 |
| 10-25 00:35 | +10 stop | ETH | UP | 0.62 | 0.80 | 1.51 |
| 10-25 00:35 | +10 stop | HYPE | UP | 0.69 | 0.52 | -2.03 |
| 10-25 00:35 | +10 stop | ZEC | UP | 0.69 | 0.51 | -2.09 |
| 10-25 00:35 | +5 | ZEC | UP | 0.69 | open |  |
| 10-25 00:34 | +10 stop | NEAR | UP | 0.66 | 0.50 | -1.94 |
| 10-25 00:34 | +10 stop | SOL | UP | 0.67 | 0.46 | -2.44 |
| 10-25 00:34 | +10 stop | ETH | DOWN | 0.52 | 0.30 | -2.53 |
| 10-25 00:34 | +10 stop | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-25 00:34 | +10 | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-25 00:34 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 10-25 00:34 | +10 | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-25 00:33 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 10-25 00:33 | +10 stop | SOL | UP | 0.71 | 0.56 | -1.83 |
| 10-25 00:33 | +5 | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 10-25 00:33 | +5 | HYPE | DOWN | 0.54 | 0.76 | 1.89 |
| 10-25 00:32 | +10 stop | ETH | DOWN | 0.64 | 0.49 | -1.85 |
