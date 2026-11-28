# Range-Scalp Bot

*Updated Sat Nov 28 09:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74454 | 64988 | 9466 (171) | 3 | $-19758.50 | -4.2% |
| **+10¢** | 55472 | 44410 | 11062 (217) | 3 | $-18391.15 | -5.3% |
| **+15¢** | 46444 | 34531 | 11913 (275) | 4 | $-16449.53 | -5.6% |
| **+20¢** | 41327 | 28782 | 12545 (343) | 4 | $-14848.88 | -5.7% |
| **+10¢ (15¢ stop)** | 90616 | 90396 | 220 (136) | 3 | $-33472.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 09:30 | +10 stop | NEAR | UP | 0.60 | 0.71 | 0.78 |
| 11-28 09:30 | +20 | NEAR | UP | 0.60 | open |  |
| 11-28 09:30 | +15 | NEAR | UP | 0.60 | open |  |
| 11-28 09:30 | +10 | NEAR | UP | 0.60 | 0.71 | 0.78 |
| 11-28 09:30 | +5 | NEAR | UP | 0.60 | 0.68 | 0.47 |
| 11-28 09:30 | +10 stop | HYPE | UP | 0.64 | open |  |
| 11-28 09:30 | +20 | HYPE | UP | 0.64 | open |  |
| 11-28 09:30 | +15 | HYPE | UP | 0.64 | open |  |
| 11-28 09:30 | +10 | HYPE | UP | 0.64 | open |  |
| 11-28 09:30 | +5 | HYPE | UP | 0.66 | open |  |
| 11-28 09:30 | +10 stop | BTC | UP | 0.65 | open |  |
| 11-28 09:30 | +20 | BTC | UP | 0.65 | open |  |
| 11-28 09:30 | +15 | BTC | UP | 0.65 | open |  |
| 11-28 09:30 | +10 | BTC | UP | 0.65 | open |  |
| 11-28 09:30 | +5 | BTC | UP | 0.65 | open |  |
| 11-28 09:30 | +10 stop | ETH | UP | 0.65 | open |  |
| 11-28 09:30 | +20 | ETH | UP | 0.65 | open |  |
| 11-28 09:30 | +15 | ETH | UP | 0.65 | open |  |
| 11-28 09:30 | +10 | ETH | UP | 0.65 | open |  |
| 11-28 09:30 | +5 | ETH | UP | 0.65 | open |  |
| 11-28 09:28 | +5 | BTC | UP | 0.63 | 0.97 | 3.26 |
| 11-28 09:28 | +5 | BTC | UP | 0.44 | 0.66 | 1.86 |
| 11-28 09:28 | +10 stop | BTC | UP | 0.63 | 0.97 | 3.26 |
| 11-28 09:27 | +10 stop | ZEC | DOWN | 0.56 | 0.74 | 1.48 |
| 11-28 09:26 | +10 stop | SOL | DOWN | 0.57 | 0.40 | -2.05 |
| 11-28 09:26 | +10 stop | ETH | DOWN | 0.53 | 0.23 | -3.31 |
| 11-28 09:25 | +10 stop | ZEC | UP | 0.34 | 0.56 | 1.86 |
| 11-28 09:25 | +10 stop | XRP | UP | 0.68 | 0.52 | -1.93 |
| 11-28 09:24 | +10 stop | BTC | DOWN | 0.68 | 0.42 | -2.94 |
| 11-28 09:24 | +10 stop | ZEC | UP | 0.71 | 0.55 | -1.93 |
| 11-28 09:24 | +15 | ZEC | UP | 0.71 | no | -7.25 |
| 11-28 09:24 | +10 | ZEC | UP | 0.71 | no | -7.25 |
| 11-28 09:24 | +5 | ZEC | UP | 0.71 | no | -7.25 |
| 11-28 09:23 | +10 stop | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-28 09:22 | +10 stop | XRP | UP | 0.60 | 0.45 | -1.85 |
| 11-28 09:21 | +10 stop | SOL | UP | 0.58 | 0.38 | -2.35 |
| 11-28 09:21 | +10 stop | ETH | UP | 0.65 | 0.44 | -2.41 |
| 11-28 09:21 | +10 stop | BNB | UP | 0.71 | 0.81 | 0.74 |
| 11-28 09:21 | +10 stop | NEAR | UP | 0.52 | 0.35 | -1.99 |
| 11-28 09:21 | +10 stop | BTC | DOWN | 0.50 | 0.67 | 1.36 |
