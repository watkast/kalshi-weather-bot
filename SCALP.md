# Range-Scalp Bot

*Updated Fri Oct 30 08:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40455 | 35321 | 5134 (51) | 1 | $-11217.64 | -4.4% |
| **+10¢** | 30145 | 24205 | 5940 (74) | 1 | $-9979.11 | -5.3% |
| **+15¢** | 25205 | 18812 | 6393 (101) | 2 | $-8992.49 | -5.7% |
| **+20¢** | 22372 | 15671 | 6701 (130) | 1 | $-7906.25 | -5.6% |
| **+10¢ (15¢ stop)** | 49342 | 49272 | 70 (37) | 0 | $-18656.12 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 08:10 | +10 stop | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 10-30 08:10 | +20 | DOGE | UP | 0.69 | 0.89 | 1.78 |
| 10-30 08:10 | +10 | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 10-30 08:10 | +5 | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 10-30 08:10 | +10 stop | XRP | DOWN | 0.64 | 0.45 | -2.25 |
| 10-30 08:10 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-30 08:10 | +15 | XRP | DOWN | 0.63 | open |  |
| 10-30 08:10 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-30 08:10 | +5 | XRP | DOWN | 0.63 | open |  |
| 10-30 08:07 | +10 stop | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-30 08:06 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 10-30 08:06 | +10 | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 10-30 08:06 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 10-30 08:05 | +10 stop | DOGE | DOWN | 0.66 | 0.50 | -1.94 |
| 10-30 08:05 | +15 | DOGE | DOWN | 0.66 | open |  |
| 10-30 08:05 | +10 | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 08:05 | +5 | DOGE | DOWN | 0.66 | 0.75 | 0.60 |
| 10-30 08:05 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-30 08:05 | +10 stop | BNB | UP | 0.60 | 0.15 | -4.76 |
| 10-30 08:04 | +5 | XRP | DOWN | 0.56 | 0.62 | 0.25 |
| 10-30 08:04 | +10 stop | BNB | UP | 0.56 | 0.66 | 0.66 |
| 10-30 08:04 | +10 stop | HYPE | DOWN | 0.61 | 0.73 | 0.89 |
| 10-30 08:04 | +20 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-30 08:04 | +15 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-30 08:04 | +10 | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-30 08:04 | +5 | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-30 08:03 | +5 | DOGE | DOWN | 0.67 | 0.76 | 0.61 |
| 10-30 08:03 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-30 08:02 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-30 08:02 | +10 | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-30 08:02 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-30 08:01 | +10 stop | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-30 08:01 | +20 | DOGE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-30 08:01 | +15 | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-30 08:01 | +10 | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-30 08:01 | +5 | DOGE | DOWN | 0.59 | 0.66 | 0.37 |
| 10-30 08:01 | +10 stop | HYPE | DOWN | 0.52 | 0.71 | 1.57 |
| 10-30 08:01 | +20 | HYPE | DOWN | 0.52 | 0.75 | 1.98 |
| 10-30 08:01 | +15 | HYPE | DOWN | 0.52 | 0.71 | 1.57 |
| 10-30 08:01 | +10 | HYPE | DOWN | 0.52 | 0.71 | 1.57 |
