# Range-Scalp Bot

*Updated Fri Nov 27 01:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73180 | 63868 | 9312 (159) | 5 | $-19538.12 | -4.2% |
| **+10¢** | 54555 | 43683 | 10872 (205) | 6 | $-18122.91 | -5.3% |
| **+15¢** | 45686 | 33973 | 11713 (263) | 6 | $-16234.72 | -5.7% |
| **+20¢** | 40660 | 28326 | 12334 (329) | 6 | $-14628.72 | -5.7% |
| **+10¢ (15¢ stop)** | 89133 | 88924 | 209 (128) | 3 | $-32903.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 01:22 | +5 | BNB | UP | 0.59 | open |  |
| 11-27 01:22 | +10 stop | SOL | UP | 0.59 | 0.42 | -2.05 |
| 11-27 01:21 | +10 stop | BNB | UP | 0.65 | open |  |
| 11-27 01:19 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 11-27 01:18 | +10 stop | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-27 01:18 | +10 stop | ETH | DOWN | 0.70 | open |  |
| 11-27 01:18 | +10 stop | XRP | DOWN | 0.67 | open |  |
| 11-27 01:17 | +10 stop | BNB | DOWN | 0.55 | 0.35 | -2.34 |
| 11-27 01:17 | +10 stop | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 11-27 01:17 | +10 stop | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 11-27 01:17 | +20 | ZEC | UP | 0.65 | 0.85 | 1.75 |
| 11-27 01:17 | +15 | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-27 01:17 | +10 | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 11-27 01:17 | +5 | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 11-27 01:16 | +10 stop | BTC | UP | 0.61 | 0.41 | -2.34 |
| 11-27 01:16 | +20 | BTC | UP | 0.61 | open |  |
| 11-27 01:16 | +15 | BTC | UP | 0.61 | open |  |
| 11-27 01:16 | +10 | BTC | UP | 0.61 | open |  |
| 11-27 01:16 | +5 | BTC | UP | 0.61 | open |  |
| 11-27 01:16 | +5 | BNB | UP | 0.62 | 0.67 | 0.17 |
| 11-27 01:16 | +10 stop | ETH | UP | 0.57 | 0.36 | -2.45 |
| 11-27 01:16 | +20 | ETH | UP | 0.57 | open |  |
| 11-27 01:16 | +15 | ETH | UP | 0.57 | open |  |
| 11-27 01:16 | +10 | ETH | UP | 0.57 | open |  |
| 11-27 01:16 | +5 | ETH | UP | 0.57 | open |  |
| 11-27 01:16 | +10 stop | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 11-27 01:16 | +20 | NEAR | UP | 0.61 | open |  |
| 11-27 01:16 | +15 | NEAR | UP | 0.61 | open |  |
| 11-27 01:16 | +10 | NEAR | UP | 0.61 | open |  |
| 11-27 01:16 | +5 | NEAR | UP | 0.61 | 0.68 | 0.37 |
| 11-27 01:16 | +10 stop | SOL | UP | 0.68 | 0.53 | -1.84 |
| 11-27 01:16 | +20 | SOL | UP | 0.68 | open |  |
| 11-27 01:16 | +15 | SOL | UP | 0.68 | open |  |
| 11-27 01:16 | +10 | SOL | UP | 0.68 | open |  |
| 11-27 01:16 | +5 | SOL | UP | 0.68 | open |  |
| 11-27 01:16 | +10 stop | XRP | UP | 0.63 | 0.47 | -1.95 |
| 11-27 01:16 | +20 | XRP | UP | 0.63 | open |  |
| 11-27 01:16 | +15 | XRP | UP | 0.63 | open |  |
| 11-27 01:16 | +10 | XRP | UP | 0.63 | open |  |
| 11-27 01:16 | +5 | XRP | UP | 0.63 | open |  |
