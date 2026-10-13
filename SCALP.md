# Range-Scalp Bot

*Updated Tue Oct 13 00:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14045 | 12151 | 1894 (26) | 6 | $-4497.32 | -5.1% |
| **+10¢** | 10630 | 8426 | 2204 (38) | 6 | $-4246.77 | -6.3% |
| **+15¢** | 8926 | 6569 | 2357 (56) | 7 | $-3781.76 | -6.8% |
| **+20¢** | 7943 | 5489 | 2454 (71) | 7 | $-3233.72 | -6.5% |
| **+10¢ (15¢ stop)** | 17234 | 17185 | 49 (29) | 2 | $-6702.16 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 00:05 | +10 stop | DOGE | DOWN | 0.71 | open |  |
| 10-13 00:04 | +10 | NEAR | DOWN | 0.60 | open |  |
| 10-13 00:04 | +5 | NEAR | DOWN | 0.58 | open |  |
| 10-13 00:04 | +10 stop | NEAR | DOWN | 0.56 | open |  |
| 10-13 00:04 | +5 | NEAR | DOWN | 0.56 | 0.61 | 0.15 |
| 10-13 00:04 | +5 | SOL | UP | 0.69 | open |  |
| 10-13 00:03 | +10 stop | BNB | UP | 0.62 | 0.41 | -2.44 |
| 10-13 00:03 | +10 | BNB | UP | 0.62 | open |  |
| 10-13 00:03 | +5 | BNB | UP | 0.62 | open |  |
| 10-13 00:03 | +5 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-13 00:03 | +5 | DOGE | UP | 0.67 | open |  |
| 10-13 00:02 | +5 | BTC | UP | 0.66 | open |  |
| 10-13 00:02 | +5 | BNB | UP | 0.57 | 0.65 | 0.46 |
| 10-13 00:02 | +10 stop | DOGE | UP | 0.60 | 0.39 | -2.44 |
| 10-13 00:02 | +20 | DOGE | UP | 0.60 | open |  |
| 10-13 00:02 | +15 | DOGE | UP | 0.60 | open |  |
| 10-13 00:02 | +10 | DOGE | UP | 0.60 | open |  |
| 10-13 00:02 | +5 | DOGE | UP | 0.60 | 0.66 | 0.27 |
| 10-13 00:02 | +10 stop | SOL | UP | 0.66 | 0.45 | -2.44 |
| 10-13 00:02 | +20 | SOL | UP | 0.66 | open |  |
| 10-13 00:02 | +15 | SOL | UP | 0.67 | open |  |
| 10-13 00:02 | +10 | SOL | UP | 0.67 | open |  |
| 10-13 00:02 | +5 | SOL | UP | 0.67 | 0.74 | 0.43 |
| 10-13 00:02 | +5 | ETH | UP | 0.68 | open |  |
| 10-13 00:01 | +10 stop | XRP | UP | 0.67 | 0.79 | 0.92 |
| 10-13 00:01 | +20 | XRP | UP | 0.67 | open |  |
| 10-13 00:01 | +15 | XRP | UP | 0.67 | open |  |
| 10-13 00:01 | +10 | XRP | UP | 0.67 | 0.79 | 0.92 |
| 10-13 00:01 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 10-13 00:01 | +10 stop | NEAR | DOWN | 0.46 | 0.56 | 0.64 |
| 10-13 00:01 | +20 | NEAR | DOWN | 0.46 | open |  |
| 10-13 00:01 | +15 | NEAR | DOWN | 0.48 | open |  |
| 10-13 00:01 | +10 | NEAR | DOWN | 0.50 | 0.61 | 0.75 |
| 10-13 00:01 | +5 | NEAR | DOWN | 0.50 | 0.56 | 0.24 |
| 10-13 00:01 | +10 stop | HYPE | DOWN | 0.59 | 0.72 | 0.98 |
| 10-13 00:01 | +20 | HYPE | DOWN | 0.59 | 0.80 | 1.81 |
| 10-13 00:01 | +15 | HYPE | DOWN | 0.59 | 0.78 | 1.60 |
| 10-13 00:01 | +10 | HYPE | DOWN | 0.59 | 0.72 | 0.98 |
| 10-13 00:01 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 10-13 00:01 | +10 stop | ZEC | DOWN | 0.62 | 0.75 | 0.96 |
