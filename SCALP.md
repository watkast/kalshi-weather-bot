# Range-Scalp Bot

*Updated Wed Nov 11 12:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55810 | 48676 | 7134 (94) | 5 | $-15202.04 | -4.3% |
| **+10¢** | 41701 | 33382 | 8319 (124) | 5 | $-14123.13 | -5.4% |
| **+15¢** | 34964 | 25989 | 8975 (158) | 6 | $-12890.62 | -5.9% |
| **+20¢** | 31139 | 21725 | 9414 (208) | 7 | $-11254.75 | -5.8% |
| **+10¢ (15¢ stop)** | 67994 | 67873 | 121 (73) | 1 | $-25005.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 12:25 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 12:24 | +10 stop | ETH | UP | 0.48 | 0.59 | 0.75 |
| 11-11 12:24 | +20 | ETH | UP | 0.48 | open |  |
| 11-11 12:24 | +15 | ETH | UP | 0.48 | open |  |
| 11-11 12:24 | +10 | ETH | UP | 0.48 | 0.59 | 0.75 |
| 11-11 12:24 | +5 | ETH | UP | 0.48 | 0.59 | 0.75 |
| 11-11 12:23 | +10 stop | XRP | UP | 0.67 | 0.44 | -2.64 |
| 11-11 12:23 | +10 stop | SOL | UP | 0.71 | 0.49 | -2.53 |
| 11-11 12:23 | +20 | SOL | UP | 0.71 | open |  |
| 11-11 12:23 | +15 | SOL | UP | 0.71 | open |  |
| 11-11 12:23 | +10 | SOL | UP | 0.71 | open |  |
| 11-11 12:23 | +5 | SOL | UP | 0.71 | open |  |
| 11-11 12:23 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 11-11 12:22 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-11 12:22 | +10 stop | HYPE | UP | 0.64 | 0.48 | -1.95 |
| 11-11 12:22 | +10 | HYPE | UP | 0.64 | open |  |
| 11-11 12:22 | +5 | HYPE | UP | 0.64 | open |  |
| 11-11 12:21 | +5 | DOGE | UP | 0.59 | open |  |
| 11-11 12:21 | +5 | ZEC | UP | 0.71 | open |  |
| 11-11 12:21 | +10 stop | NEAR | UP | 0.63 | 0.48 | -1.85 |
| 11-11 12:21 | +10 stop | ZEC | UP | 0.71 | 0.50 | -2.43 |
| 11-11 12:21 | +20 | ZEC | UP | 0.71 | open |  |
| 11-11 12:21 | +15 | ZEC | UP | 0.71 | open |  |
| 11-11 12:21 | +10 | ZEC | UP | 0.71 | open |  |
| 11-11 12:20 | +10 stop | XRP | UP | 0.65 | 0.75 | 0.70 |
| 11-11 12:20 | +10 stop | DOGE | UP | 0.51 | 0.31 | -2.32 |
| 11-11 12:20 | +10 | DOGE | UP | 0.51 | open |  |
| 11-11 12:20 | +5 | DOGE | UP | 0.51 | 0.56 | 0.15 |
| 11-11 12:20 | +10 stop | NEAR | UP | 0.49 | 0.60 | 0.75 |
| 11-11 12:18 | +10 stop | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 11-11 12:18 | +20 | DOGE | UP | 0.58 | open |  |
| 11-11 12:18 | +15 | DOGE | UP | 0.58 | open |  |
| 11-11 12:18 | +10 | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 11-11 12:18 | +5 | DOGE | UP | 0.58 | 0.65 | 0.32 |
| 11-11 12:18 | +10 stop | HYPE | UP | 0.68 | 0.80 | 0.92 |
| 11-11 12:18 | +20 | HYPE | UP | 0.68 | open |  |
| 11-11 12:18 | +15 | HYPE | UP | 0.68 | open |  |
| 11-11 12:18 | +10 | HYPE | UP | 0.68 | 0.80 | 0.92 |
| 11-11 12:18 | +5 | HYPE | UP | 0.68 | 0.80 | 0.92 |
| 11-11 12:18 | +10 stop | SOL | UP | 0.66 | 0.78 | 0.91 |
