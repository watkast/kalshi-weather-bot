# Range-Scalp Bot

*Updated Tue Nov 24 20:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71015 | 61985 | 9030 (155) | 7 | $-18929.29 | -4.2% |
| **+10¢** | 52974 | 42428 | 10546 (201) | 9 | $-17530.27 | -5.3% |
| **+15¢** | 44362 | 33005 | 11357 (258) | 8 | $-15606.99 | -5.6% |
| **+20¢** | 39496 | 27540 | 11956 (324) | 9 | $-13978.39 | -5.6% |
| **+10¢ (15¢ stop)** | 86452 | 86251 | 201 (121) | 8 | $-31789.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 20:06 | +5 | ETH | DOWN | 0.60 | open |  |
| 11-24 20:06 | +10 stop | BNB | UP | 0.62 | open |  |
| 11-24 20:06 | +10 stop | NEAR | UP | 0.70 | open |  |
| 11-24 20:05 | +10 stop | ETH | DOWN | 0.48 | open |  |
| 11-24 20:05 | +10 | ETH | DOWN | 0.48 | open |  |
| 11-24 20:05 | +5 | ETH | DOWN | 0.47 | 0.54 | 0.34 |
| 11-24 20:05 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-24 20:05 | +5 | XRP | UP | 0.67 | 0.72 | 0.19 |
| 11-24 20:05 | +10 stop | DOGE | UP | 0.67 | open |  |
| 11-24 20:05 | +10 | DOGE | UP | 0.67 | open |  |
| 11-24 20:05 | +10 stop | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 11-24 20:05 | +10 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 11-24 20:05 | +5 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 11-24 20:05 | +10 stop | SOL | UP | 0.63 | open |  |
| 11-24 20:04 | +5 | DOGE | UP | 0.66 | open |  |
| 11-24 20:04 | +5 | HYPE | DOWN | 0.68 | open |  |
| 11-24 20:04 | +10 stop | XRP | UP | 0.51 | 0.62 | 0.77 |
| 11-24 20:04 | +15 | XRP | UP | 0.51 | 0.72 | 1.79 |
| 11-24 20:04 | +5 | XRP | UP | 0.51 | 0.62 | 0.77 |
| 11-24 20:04 | +10 stop | BNB | DOWN | 0.68 | 0.51 | -2.04 |
| 11-24 20:04 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-24 20:04 | +15 | BNB | DOWN | 0.68 | open |  |
| 11-24 20:04 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-24 20:04 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-24 20:04 | +10 stop | BTC | DOWN | 0.69 | open |  |
| 11-24 20:04 | +5 | BTC | DOWN | 0.68 | open |  |
| 11-24 20:03 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-24 20:03 | +10 stop | DOGE | UP | 0.56 | 0.66 | 0.66 |
| 11-24 20:03 | +20 | DOGE | UP | 0.56 | open |  |
| 11-24 20:03 | +15 | DOGE | UP | 0.56 | open |  |
| 11-24 20:03 | +10 | DOGE | UP | 0.56 | 0.66 | 0.66 |
| 11-24 20:03 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 11-24 20:03 | +5 | NEAR | DOWN | 0.56 | open |  |
| 11-24 20:02 | +10 | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 11-24 20:02 | +5 | SOL | DOWN | 0.61 | open |  |
| 11-24 20:02 | +10 stop | NEAR | DOWN | 0.52 | 0.36 | -1.95 |
| 11-24 20:02 | +20 | NEAR | DOWN | 0.52 | open |  |
| 11-24 20:02 | +15 | NEAR | DOWN | 0.52 | open |  |
| 11-24 20:02 | +10 | NEAR | DOWN | 0.52 | open |  |
| 11-24 20:02 | +5 | NEAR | DOWN | 0.53 | 0.59 | 0.25 |
