# Range-Scalp Bot

*Updated Sat Oct 31 14:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42372 | 36961 | 5411 (59) | 2 | $-11905.01 | -4.5% |
| **+10¢** | 31595 | 25331 | 6264 (81) | 2 | $-10693.69 | -5.4% |
| **+15¢** | 26422 | 19668 | 6754 (109) | 3 | $-9790.73 | -5.9% |
| **+20¢** | 23462 | 16385 | 7077 (141) | 5 | $-8651.19 | -5.9% |
| **+10¢ (15¢ stop)** | 51664 | 51585 | 79 (44) | 0 | $-19501.03 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 14:56 | +10 stop | SOL | UP | 0.67 | 0.41 | -2.93 |
| 10-31 14:56 | +20 | SOL | UP | 0.67 | open |  |
| 10-31 14:56 | +15 | SOL | UP | 0.68 | open |  |
| 10-31 14:56 | +10 | SOL | UP | 0.67 | open |  |
| 10-31 14:56 | +5 | SOL | UP | 0.67 | open |  |
| 10-31 14:55 | +10 stop | ZEC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-31 14:55 | +15 | ZEC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-31 14:55 | +10 | ZEC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-31 14:55 | +5 | ZEC | DOWN | 0.66 | 0.75 | 0.60 |
| 10-31 14:55 | +10 stop | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 10-31 14:55 | +10 | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 10-31 14:55 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-31 14:55 | +10 stop | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-31 14:55 | +20 | DOGE | UP | 0.60 | open |  |
| 10-31 14:55 | +15 | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-31 14:55 | +10 | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-31 14:55 | +5 | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-31 14:54 | +10 stop | BTC | UP | 0.53 | 0.65 | 0.86 |
| 10-31 14:54 | +10 | BTC | UP | 0.52 | 0.65 | 0.96 |
| 10-31 14:54 | +5 | BTC | UP | 0.52 | 0.65 | 0.96 |
| 10-31 14:54 | +10 | NEAR | UP | 0.54 | open |  |
| 10-31 14:54 | +5 | NEAR | UP | 0.54 | open |  |
| 10-31 14:54 | +10 stop | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-31 14:54 | +15 | HYPE | DOWN | 0.62 | 0.81 | 1.58 |
| 10-31 14:54 | +10 | HYPE | DOWN | 0.62 | 0.81 | 1.58 |
| 10-31 14:54 | +5 | HYPE | DOWN | 0.62 | 0.81 | 1.58 |
| 10-31 14:53 | +10 stop | NEAR | DOWN | 0.46 | 0.70 | 2.07 |
| 10-31 14:52 | +10 stop | XRP | UP | 0.70 | 0.88 | 1.57 |
| 10-31 14:52 | +20 | XRP | UP | 0.70 | 0.92 | 2.03 |
| 10-31 14:52 | +15 | XRP | UP | 0.70 | 0.88 | 1.57 |
| 10-31 14:52 | +10 | XRP | UP | 0.70 | 0.88 | 1.57 |
| 10-31 14:52 | +5 | XRP | UP | 0.70 | 0.88 | 1.57 |
| 10-31 14:52 | +5 | ZEC | UP | 0.65 | 0.72 | 0.39 |
| 10-31 14:51 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-31 14:51 | +20 | DOGE | UP | 0.69 | 0.91 | 1.93 |
| 10-31 14:51 | +15 | DOGE | UP | 0.69 | 0.86 | 1.46 |
| 10-31 14:51 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-31 14:51 | +5 | DOGE | UP | 0.70 | 0.79 | 0.63 |
| 10-31 14:51 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 0.98 |
| 10-31 14:51 | +10 stop | ZEC | UP | 0.59 | 0.72 | 0.98 |
