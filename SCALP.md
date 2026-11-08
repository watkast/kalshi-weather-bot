# Range-Scalp Bot

*Updated Sun Nov 08 03:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51945 | 45295 | 6650 (80) | 3 | $-14392.88 | -4.4% |
| **+10¢** | 38765 | 31009 | 7756 (106) | 5 | $-13410.44 | -5.5% |
| **+15¢** | 32463 | 24105 | 8358 (135) | 6 | $-12297.12 | -6.0% |
| **+20¢** | 28876 | 20114 | 8762 (180) | 8 | $-10836.86 | -6.0% |
| **+10¢ (15¢ stop)** | 63251 | 63148 | 103 (61) | 2 | $-23401.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 03:55 | +5 | XRP | DOWN | 0.63 | open |  |
| 11-08 03:54 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-08 03:53 | +10 stop | XRP | DOWN | 0.52 | open |  |
| 11-08 03:53 | +15 | XRP | DOWN | 0.52 | open |  |
| 11-08 03:53 | +10 | XRP | DOWN | 0.52 | open |  |
| 11-08 03:53 | +5 | XRP | DOWN | 0.52 | 0.57 | 0.14 |
| 11-08 03:53 | +10 stop | ZEC | UP | 0.58 | 0.26 | -3.52 |
| 11-08 03:53 | +20 | ZEC | UP | 0.58 | open |  |
| 11-08 03:53 | +15 | ZEC | UP | 0.58 | open |  |
| 11-08 03:53 | +10 | ZEC | UP | 0.58 | open |  |
| 11-08 03:53 | +5 | ZEC | UP | 0.58 | open |  |
| 11-08 03:53 | +5 | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 11-08 03:53 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-08 03:53 | +10 | HYPE | DOWN | 0.68 | 0.79 | 0.78 |
| 11-08 03:53 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.26 |
| 11-08 03:52 | +10 stop | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 11-08 03:52 | +10 | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 11-08 03:52 | +10 stop | NEAR | UP | 0.57 | 0.40 | -2.05 |
| 11-08 03:52 | +20 | NEAR | UP | 0.57 | open |  |
| 11-08 03:52 | +15 | NEAR | UP | 0.57 | open |  |
| 11-08 03:52 | +10 | NEAR | UP | 0.57 | open |  |
| 11-08 03:52 | +5 | NEAR | UP | 0.57 | open |  |
| 11-08 03:52 | +5 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 11-08 03:52 | +10 stop | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 11-08 03:52 | +20 | HYPE | UP | 0.57 | open |  |
| 11-08 03:52 | +15 | HYPE | UP | 0.57 | open |  |
| 11-08 03:52 | +10 | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 11-08 03:52 | +5 | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 11-08 03:52 | +10 stop | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-08 03:52 | +5 | DOGE | DOWN | 0.55 | 0.64 | 0.55 |
| 11-08 03:52 | +10 stop | BTC | UP | 0.69 | open |  |
| 11-08 03:52 | +20 | BTC | UP | 0.69 | open |  |
| 11-08 03:52 | +15 | BTC | UP | 0.69 | open |  |
| 11-08 03:52 | +10 | BTC | UP | 0.69 | open |  |
| 11-08 03:52 | +5 | BTC | UP | 0.69 | 0.75 | 0.31 |
| 11-08 03:52 | +10 stop | SOL | DOWN | 0.52 | 0.62 | 0.65 |
| 11-08 03:52 | +15 | SOL | DOWN | 0.52 | 0.74 | 1.88 |
| 11-08 03:52 | +10 | SOL | DOWN | 0.52 | 0.62 | 0.65 |
| 11-08 03:52 | +5 | SOL | DOWN | 0.52 | 0.58 | 0.24 |
| 11-08 03:52 | +10 stop | ETH | DOWN | 0.52 | 0.75 | 1.98 |
