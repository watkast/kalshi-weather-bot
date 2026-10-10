# Range-Scalp Bot

*Updated Sat Oct 10 20:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10838 | 9339 | 1499 (22) | 3 | $-3729.25 | -5.5% |
| **+10¢** | 8206 | 6462 | 1744 (36) | 5 | $-3547.72 | -6.9% |
| **+15¢** | 6923 | 5077 | 1846 (52) | 5 | $-3006.69 | -6.9% |
| **+20¢** | 6156 | 4233 | 1923 (66) | 5 | $-2564.07 | -6.6% |
| **+10¢ (15¢ stop)** | 13343 | 13302 | 41 (25) | 3 | $-5335.45 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 20:20 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 10-10 20:19 | +10 stop | NEAR | UP | 0.55 | open |  |
| 10-10 20:19 | +10 stop | BTC | UP | 0.55 | 0.39 | -1.95 |
| 10-10 20:19 | +10 stop | DOGE | DOWN | 0.53 | 0.75 | 1.89 |
| 10-10 20:19 | +20 | DOGE | DOWN | 0.53 | 0.75 | 1.89 |
| 10-10 20:19 | +15 | DOGE | DOWN | 0.53 | 0.75 | 1.89 |
| 10-10 20:19 | +10 | DOGE | DOWN | 0.53 | 0.75 | 1.89 |
| 10-10 20:19 | +5 | DOGE | DOWN | 0.53 | 0.62 | 0.56 |
| 10-10 20:18 | +10 stop | BNB | DOWN | 0.71 | 0.49 | -2.51 |
| 10-10 20:18 | +20 | BNB | DOWN | 0.67 | open |  |
| 10-10 20:18 | +15 | BNB | DOWN | 0.68 | open |  |
| 10-10 20:18 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-10 20:18 | +5 | BNB | DOWN | 0.68 | open |  |
| 10-10 20:18 | +10 stop | NEAR | DOWN | 0.65 | 0.50 | -1.84 |
| 10-10 20:18 | +5 | BTC | DOWN | 0.58 | open |  |
| 10-10 20:17 | +10 stop | XRP | DOWN | 0.64 | 0.42 | -2.55 |
| 10-10 20:17 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-10 20:17 | +15 | XRP | DOWN | 0.64 | open |  |
| 10-10 20:17 | +10 | XRP | DOWN | 0.64 | open |  |
| 10-10 20:17 | +5 | XRP | DOWN | 0.64 | 0.73 | 0.59 |
| 10-10 20:16 | +10 stop | BTC | DOWN | 0.70 | 0.51 | -2.23 |
| 10-10 20:16 | +20 | BTC | DOWN | 0.70 | open |  |
| 10-10 20:16 | +15 | BTC | DOWN | 0.70 | open |  |
| 10-10 20:16 | +10 | BTC | DOWN | 0.70 | open |  |
| 10-10 20:16 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-10 20:16 | +10 stop | HYPE | DOWN | 0.69 | open |  |
| 10-10 20:16 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-10 20:16 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-10 20:16 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-10 20:16 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.47 |
| 10-10 20:16 | +10 stop | NEAR | UP | 0.53 | 0.38 | -1.85 |
| 10-10 20:16 | +20 | NEAR | UP | 0.53 | open |  |
| 10-10 20:16 | +15 | NEAR | UP | 0.51 | open |  |
| 10-10 20:16 | +10 | NEAR | UP | 0.51 | open |  |
| 10-10 20:16 | +5 | NEAR | UP | 0.51 | open |  |
| 10-10 20:12 | +10 stop | DOGE | DOWN | 0.68 | 0.94 | 2.42 |
| 10-10 20:12 | +5 | DOGE | DOWN | 0.68 | 0.94 | 2.42 |
| 10-10 20:11 | +10 stop | HYPE | UP | 0.45 | 0.60 | 1.15 |
| 10-10 20:11 | +20 | HYPE | UP | 0.45 | no | -4.68 |
| 10-10 20:11 | +5 | HYPE | UP | 0.46 | 0.60 | 1.05 |
