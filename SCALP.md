# Range-Scalp Bot

*Updated Fri Nov 06 12:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49456 | 43095 | 6361 (76) | 1 | $-14010.59 | -4.5% |
| **+10¢** | 36920 | 29524 | 7396 (101) | 1 | $-12891.76 | -5.6% |
| **+15¢** | 30927 | 22963 | 7964 (130) | 1 | $-11771.49 | -6.1% |
| **+20¢** | 27495 | 19148 | 8347 (171) | 1 | $-10396.52 | -6.0% |
| **+10¢ (15¢ stop)** | 60294 | 60197 | 97 (57) | 0 | $-22362.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 12:41 | +10 stop | HYPE | UP | 0.67 | 0.52 | -1.84 |
| 11-06 12:41 | +5 | HYPE | UP | 0.70 | open |  |
| 11-06 12:40 | +10 stop | HYPE | DOWN | 0.57 | 0.39 | -2.15 |
| 11-06 12:39 | +10 stop | HYPE | UP | 0.60 | 0.40 | -2.34 |
| 11-06 12:39 | +20 | HYPE | UP | 0.58 | open |  |
| 11-06 12:39 | +15 | HYPE | UP | 0.58 | open |  |
| 11-06 12:39 | +10 | HYPE | UP | 0.58 | open |  |
| 11-06 12:39 | +5 | HYPE | UP | 0.58 | 0.65 | 0.36 |
| 11-06 12:32 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-06 12:32 | +20 | ETH | DOWN | 0.60 | 0.81 | 1.82 |
| 11-06 12:32 | +15 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 11-06 12:32 | +10 | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-06 12:32 | +5 | ETH | DOWN | 0.59 | 0.74 | 1.19 |
| 11-06 12:32 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-06 12:32 | +20 | HYPE | DOWN | 0.70 | 0.90 | 1.79 |
| 11-06 12:32 | +15 | HYPE | DOWN | 0.70 | 0.87 | 1.47 |
| 11-06 12:32 | +10 | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-06 12:32 | +5 | HYPE | DOWN | 0.70 | 0.79 | 0.63 |
| 11-06 12:32 | +10 stop | SOL | DOWN | 0.69 | 0.85 | 1.36 |
| 11-06 12:32 | +20 | SOL | DOWN | 0.69 | 0.92 | 2.04 |
| 11-06 12:32 | +15 | SOL | DOWN | 0.69 | 0.85 | 1.36 |
| 11-06 12:32 | +10 | SOL | DOWN | 0.69 | 0.85 | 1.36 |
| 11-06 12:32 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 11-06 08:22 | +10 stop | DOGE | UP | 0.64 | no | -6.57 |
| 11-06 08:22 | +20 | DOGE | UP | 0.63 | no | -6.47 |
| 11-06 08:22 | +15 | DOGE | UP | 0.63 | no | -6.47 |
| 11-06 08:22 | +10 | DOGE | UP | 0.63 | no | -6.47 |
| 11-06 08:22 | +5 | DOGE | UP | 0.63 | no | -6.47 |
| 11-06 08:21 | +10 | ZEC | UP | 0.66 | no | -6.76 |
| 11-06 08:21 | +5 | ZEC | UP | 0.66 | no | -6.76 |
| 11-06 08:21 | +10 stop | ZEC | UP | 0.64 | no | -6.57 |
| 11-06 08:20 | +5 | HYPE | UP | 0.59 | 0.64 | 0.16 |
| 11-06 08:20 | +10 stop | ZEC | DOWN | 0.67 | 0.42 | -2.84 |
| 11-06 08:19 | +5 | BNB | UP | 0.71 | 0.76 | 0.22 |
| 11-06 08:19 | +10 stop | XRP | UP | 0.62 | 0.72 | 0.68 |
| 11-06 08:19 | +20 | XRP | UP | 0.62 | 0.83 | 1.83 |
| 11-06 08:19 | +15 | XRP | UP | 0.62 | 0.83 | 1.83 |
| 11-06 08:19 | +10 | XRP | UP | 0.62 | 0.72 | 0.68 |
| 11-06 08:19 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 11-06 08:18 | +5 | ETH | UP | 0.70 | 0.77 | 0.42 |
