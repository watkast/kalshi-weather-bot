# Range-Scalp Bot

*Updated Fri Oct 30 10:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40594 | 35432 | 5162 (51) | 1 | $-11333.74 | -4.4% |
| **+10¢** | 30244 | 24275 | 5969 (74) | 5 | $-10084.15 | -5.3% |
| **+15¢** | 25287 | 18862 | 6425 (101) | 5 | $-9109.81 | -5.7% |
| **+20¢** | 22446 | 15711 | 6735 (131) | 5 | $-8023.27 | -5.7% |
| **+10¢ (15¢ stop)** | 49500 | 49430 | 70 (37) | 5 | $-18748.23 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 10:01 | +10 stop | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 10-30 10:01 | +20 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 10-30 10:01 | +15 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 10-30 10:01 | +10 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 10-30 10:01 | +5 | NEAR | DOWN | 0.61 | 0.68 | 0.37 |
| 10-30 10:01 | +10 stop | ZEC | DOWN | 0.69 | open |  |
| 10-30 10:01 | +20 | ZEC | DOWN | 0.69 | open |  |
| 10-30 10:01 | +15 | ZEC | DOWN | 0.69 | open |  |
| 10-30 10:01 | +10 | ZEC | DOWN | 0.69 | open |  |
| 10-30 10:01 | +5 | ZEC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-30 10:01 | +10 stop | XRP | DOWN | 0.71 | open |  |
| 10-30 10:01 | +20 | XRP | DOWN | 0.71 | open |  |
| 10-30 10:01 | +15 | XRP | DOWN | 0.71 | open |  |
| 10-30 10:01 | +10 | XRP | DOWN | 0.71 | open |  |
| 10-30 10:01 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 10-30 10:01 | +10 stop | BNB | DOWN | 0.66 | open |  |
| 10-30 10:01 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-30 10:01 | +15 | BNB | DOWN | 0.66 | open |  |
| 10-30 10:01 | +10 | BNB | DOWN | 0.66 | open |  |
| 10-30 10:01 | +5 | BNB | DOWN | 0.66 | open |  |
| 10-30 10:01 | +10 stop | BTC | DOWN | 0.63 | open |  |
| 10-30 10:01 | +20 | BTC | DOWN | 0.63 | open |  |
| 10-30 10:01 | +15 | BTC | DOWN | 0.63 | open |  |
| 10-30 10:01 | +10 | BTC | DOWN | 0.63 | open |  |
| 10-30 10:01 | +5 | BTC | DOWN | 0.63 | 0.71 | 0.48 |
| 10-30 10:01 | +10 stop | HYPE | DOWN | 0.65 | open |  |
| 10-30 10:01 | +20 | HYPE | DOWN | 0.65 | open |  |
| 10-30 10:01 | +15 | HYPE | DOWN | 0.65 | open |  |
| 10-30 10:01 | +10 | HYPE | DOWN | 0.65 | open |  |
| 10-30 10:01 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 10-30 09:58 | +10 stop | HYPE | UP | 0.65 | 0.83 | 1.54 |
| 10-30 09:58 | +15 | HYPE | UP | 0.65 | 0.83 | 1.54 |
| 10-30 09:58 | +10 | HYPE | UP | 0.65 | 0.83 | 1.54 |
| 10-30 09:58 | +5 | HYPE | UP | 0.65 | 0.83 | 1.54 |
| 10-30 09:58 | +10 stop | HYPE | DOWN | 0.41 | 0.60 | 1.56 |
| 10-30 09:58 | +20 | HYPE | DOWN | 0.41 | yes | -4.27 |
| 10-30 09:58 | +15 | HYPE | DOWN | 0.41 | 0.60 | 1.56 |
| 10-30 09:58 | +10 | HYPE | DOWN | 0.49 | 0.60 | 0.75 |
| 10-30 09:58 | +5 | HYPE | DOWN | 0.49 | 0.60 | 0.75 |
| 10-30 09:55 | +5 | BNB | DOWN | 0.62 | 0.73 | 0.79 |
