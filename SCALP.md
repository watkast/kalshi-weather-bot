# Range-Scalp Bot

*Updated Fri Oct 30 03:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40137 | 35064 | 5073 (51) | 4 | $-10980.73 | -4.3% |
| **+10¢** | 29902 | 24031 | 5871 (74) | 5 | $-9730.85 | -5.2% |
| **+15¢** | 25011 | 18694 | 6317 (101) | 5 | $-8709.70 | -5.5% |
| **+20¢** | 22194 | 15570 | 6624 (130) | 5 | $-7629.69 | -5.5% |
| **+10¢ (15¢ stop)** | 48953 | 48883 | 70 (37) | 0 | $-18488.97 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 03:23 | +10 stop | HYPE | UP | 0.65 | 0.77 | 0.91 |
| 10-30 03:23 | +10 stop | NEAR | UP | 0.60 | 0.71 | 0.78 |
| 10-30 03:22 | +10 stop | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 10-30 03:22 | +10 | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 10-30 03:22 | +5 | DOGE | UP | 0.64 | 0.71 | 0.38 |
| 10-30 03:21 | +10 stop | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 10-30 03:21 | +10 | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 10-30 03:21 | +10 stop | SOL | UP | 0.65 | 0.81 | 1.33 |
| 10-30 03:21 | +5 | SOL | UP | 0.66 | 0.74 | 0.50 |
| 10-30 03:20 | +10 stop | ETH | UP | 0.58 | 0.73 | 1.18 |
| 10-30 03:20 | +10 stop | BTC | UP | 0.55 | 0.66 | 0.76 |
| 10-30 03:20 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-30 03:20 | +20 | DOGE | UP | 0.60 | 0.83 | 2.03 |
| 10-30 03:20 | +15 | DOGE | UP | 0.60 | 0.78 | 1.50 |
| 10-30 03:20 | +10 | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-30 03:20 | +5 | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-30 03:19 | +5 | ZEC | UP | 0.71 | 0.78 | 0.42 |
| 10-30 03:19 | +10 stop | SOL | UP | 0.66 | 0.77 | 0.81 |
| 10-30 03:18 | +5 | XRP | UP | 0.69 | 0.74 | 0.21 |
| 10-30 03:18 | +5 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-30 03:18 | +10 stop | BTC | DOWN | 0.57 | 0.30 | -3.03 |
| 10-30 03:18 | +5 | SOL | UP | 0.57 | 0.64 | 0.35 |
| 10-30 03:18 | +10 stop | ETH | UP | 0.54 | 0.69 | 1.17 |
| 10-30 03:18 | +10 stop | NEAR | DOWN | 0.56 | 0.41 | -1.85 |
| 10-30 03:18 | +20 | NEAR | DOWN | 0.56 | open |  |
| 10-30 03:18 | +15 | NEAR | DOWN | 0.56 | open |  |
| 10-30 03:18 | +10 | NEAR | DOWN | 0.56 | open |  |
| 10-30 03:18 | +5 | NEAR | DOWN | 0.56 | open |  |
| 10-30 03:17 | +5 | SOL | UP | 0.51 | 0.58 | 0.34 |
| 10-30 03:17 | +10 stop | XRP | UP | 0.65 | 0.76 | 0.81 |
| 10-30 03:17 | +20 | XRP | UP | 0.65 | 0.87 | 1.96 |
| 10-30 03:17 | +15 | XRP | UP | 0.65 | 0.82 | 1.43 |
| 10-30 03:17 | +10 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 10-30 03:17 | +5 | XRP | UP | 0.65 | 0.71 | 0.29 |
| 10-30 03:17 | +10 stop | ZEC | UP | 0.60 | 0.71 | 0.78 |
| 10-30 03:17 | +20 | ZEC | UP | 0.60 | 0.82 | 1.92 |
| 10-30 03:17 | +15 | ZEC | UP | 0.60 | 0.78 | 1.50 |
| 10-30 03:17 | +10 | ZEC | UP | 0.60 | 0.71 | 0.78 |
| 10-30 03:17 | +5 | ZEC | UP | 0.60 | 0.66 | 0.27 |
| 10-30 03:17 | +10 stop | SOL | DOWN | 0.50 | 0.35 | -1.84 |
