# Range-Scalp Bot

*Updated Fri Oct 30 12:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40713 | 35530 | 5183 (51) | 7 | $-11409.61 | -4.4% |
| **+10¢** | 30337 | 24344 | 5993 (74) | 9 | $-10163.56 | -5.3% |
| **+15¢** | 25367 | 18915 | 6452 (101) | 9 | $-9194.22 | -5.8% |
| **+20¢** | 22514 | 15751 | 6763 (131) | 9 | $-8120.68 | -5.7% |
| **+10¢ (15¢ stop)** | 49647 | 49577 | 70 (37) | 7 | $-18783.35 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 12:04 | +10 stop | DOGE | DOWN | 0.49 | 0.62 | 0.95 |
| 10-30 12:04 | +5 | DOGE | DOWN | 0.49 | 0.62 | 0.95 |
| 10-30 12:04 | +5 | NEAR | DOWN | 0.62 | open |  |
| 10-30 12:04 | +10 stop | ETH | DOWN | 0.57 | open |  |
| 10-30 12:04 | +10 | ETH | DOWN | 0.57 | open |  |
| 10-30 12:04 | +5 | ETH | DOWN | 0.57 | open |  |
| 10-30 12:04 | +10 stop | XRP | DOWN | 0.58 | open |  |
| 10-30 12:04 | +10 stop | HYPE | DOWN | 0.68 | open |  |
| 10-30 12:04 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-30 12:04 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-30 12:04 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-30 12:04 | +5 | HYPE | DOWN | 0.69 | open |  |
| 10-30 12:03 | +20 | DOGE | UP | 0.48 | open |  |
| 10-30 12:03 | +10 stop | BTC | UP | 0.62 | open |  |
| 10-30 12:03 | +5 | DOGE | UP | 0.51 | 0.61 | 0.65 |
| 10-30 12:03 | +10 stop | ZEC | DOWN | 0.66 | open |  |
| 10-30 12:03 | +20 | ZEC | DOWN | 0.66 | open |  |
| 10-30 12:03 | +15 | ZEC | DOWN | 0.66 | open |  |
| 10-30 12:03 | +10 | ZEC | DOWN | 0.66 | open |  |
| 10-30 12:03 | +5 | ZEC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-30 12:03 | +10 stop | ETH | DOWN | 0.54 | 0.64 | 0.65 |
| 10-30 12:03 | +20 | ETH | DOWN | 0.54 | open |  |
| 10-30 12:03 | +10 | ETH | DOWN | 0.54 | 0.64 | 0.65 |
| 10-30 12:03 | +5 | ETH | DOWN | 0.54 | 0.64 | 0.65 |
| 10-30 12:03 | +10 stop | BNB | DOWN | 0.58 | open |  |
| 10-30 12:03 | +5 | SOL | DOWN | 0.57 | open |  |
| 10-30 12:03 | +10 stop | DOGE | DOWN | 0.53 | 0.38 | -1.85 |
| 10-30 12:03 | +15 | DOGE | DOWN | 0.53 | open |  |
| 10-30 12:03 | +10 | DOGE | DOWN | 0.53 | open |  |
| 10-30 12:03 | +5 | DOGE | DOWN | 0.53 | 0.58 | 0.14 |
| 10-30 12:02 | +20 | BNB | DOWN | 0.71 | open |  |
| 10-30 12:02 | +15 | BNB | DOWN | 0.71 | open |  |
| 10-30 12:02 | +10 | BNB | DOWN | 0.71 | open |  |
| 10-30 12:02 | +5 | BNB | DOWN | 0.71 | open |  |
| 10-30 12:02 | +15 | ETH | DOWN | 0.71 | open |  |
| 10-30 12:02 | +10 stop | SOL | DOWN | 0.61 | 0.43 | -2.15 |
| 10-30 12:02 | +20 | SOL | DOWN | 0.61 | open |  |
| 10-30 12:02 | +15 | SOL | DOWN | 0.61 | open |  |
| 10-30 12:02 | +10 | SOL | DOWN | 0.61 | open |  |
| 10-30 12:02 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
