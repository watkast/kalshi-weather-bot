# Range-Scalp Bot

*Updated Fri Oct 16 13:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19242 | 16717 | 2525 (29) | 6 | $-5822.23 | -4.8% |
| **+10¢** | 14507 | 11588 | 2919 (41) | 8 | $-5255.44 | -5.8% |
| **+15¢** | 12144 | 9001 | 3143 (60) | 8 | $-4776.82 | -6.3% |
| **+20¢** | 10774 | 7479 | 3295 (79) | 8 | $-4262.39 | -6.3% |
| **+10¢ (15¢ stop)** | 23664 | 23614 | 50 (29) | 6 | $-9118.91 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 13:03 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 10-16 13:02 | +5 | BTC | UP | 0.51 | 0.57 | 0.24 |
| 10-16 13:02 | +10 stop | DOGE | UP | 0.66 | open |  |
| 10-16 13:02 | +20 | DOGE | UP | 0.66 | open |  |
| 10-16 13:02 | +15 | DOGE | UP | 0.66 | open |  |
| 10-16 13:02 | +10 | DOGE | UP | 0.66 | open |  |
| 10-16 13:02 | +5 | DOGE | UP | 0.66 | open |  |
| 10-16 13:02 | +5 | BNB | UP | 0.53 | open |  |
| 10-16 13:02 | +10 stop | XRP | UP | 0.58 | open |  |
| 10-16 13:02 | +20 | XRP | UP | 0.58 | open |  |
| 10-16 13:02 | +15 | XRP | UP | 0.58 | open |  |
| 10-16 13:02 | +10 | XRP | UP | 0.57 | open |  |
| 10-16 13:02 | +5 | XRP | UP | 0.57 | open |  |
| 10-16 13:01 | +10 stop | NEAR | DOWN | 0.57 | 0.40 | -2.05 |
| 10-16 13:01 | +20 | NEAR | DOWN | 0.59 | open |  |
| 10-16 13:01 | +15 | NEAR | DOWN | 0.59 | open |  |
| 10-16 13:01 | +10 | NEAR | DOWN | 0.59 | open |  |
| 10-16 13:01 | +5 | NEAR | DOWN | 0.59 | open |  |
| 10-16 13:01 | +10 stop | ZEC | DOWN | 0.62 | 0.47 | -1.88 |
| 10-16 13:01 | +20 | ZEC | DOWN | 0.63 | open |  |
| 10-16 13:01 | +15 | ZEC | DOWN | 0.61 | open |  |
| 10-16 13:01 | +10 | ZEC | DOWN | 0.61 | open |  |
| 10-16 13:01 | +5 | ZEC | DOWN | 0.61 | open |  |
| 10-16 13:01 | +10 stop | HYPE | DOWN | 0.67 | 0.50 | -2.08 |
| 10-16 13:01 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-16 13:01 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-16 13:01 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-16 13:01 | +5 | HYPE | DOWN | 0.67 | open |  |
| 10-16 13:00 | +10 stop | ETH | UP | 0.54 | open |  |
| 10-16 13:00 | +20 | ETH | UP | 0.54 | open |  |
| 10-16 13:00 | +15 | ETH | UP | 0.54 | open |  |
| 10-16 13:00 | +10 | ETH | UP | 0.54 | open |  |
| 10-16 13:00 | +5 | ETH | UP | 0.54 | 0.60 | 0.25 |
| 10-16 13:00 | +10 stop | BNB | UP | 0.51 | open |  |
| 10-16 13:00 | +20 | BNB | UP | 0.51 | open |  |
| 10-16 13:00 | +15 | BNB | UP | 0.51 | open |  |
| 10-16 13:00 | +10 | BNB | UP | 0.51 | open |  |
| 10-16 13:00 | +5 | BNB | UP | 0.51 | 0.60 | 0.55 |
| 10-16 13:00 | +10 stop | BTC | UP | 0.55 | open |  |
| 10-16 13:00 | +20 | BTC | UP | 0.55 | open |  |
