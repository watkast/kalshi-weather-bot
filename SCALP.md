# Range-Scalp Bot

*Updated Sat Oct 31 12:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42243 | 36856 | 5387 (55) | 5 | $-11854.06 | -4.5% |
| **+10¢** | 31494 | 25256 | 6238 (79) | 5 | $-10625.33 | -5.4% |
| **+15¢** | 26338 | 19612 | 6726 (107) | 6 | $-9717.06 | -5.9% |
| **+20¢** | 23389 | 16343 | 7046 (138) | 7 | $-8573.24 | -5.8% |
| **+10¢ (15¢ stop)** | 51522 | 51447 | 75 (41) | 4 | $-19456.03 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 12:20 | +10 stop | DOGE | UP | 0.48 | open |  |
| 10-31 12:20 | +10 stop | XRP | UP | 0.59 | open |  |
| 10-31 12:20 | +5 | XRP | UP | 0.59 | open |  |
| 10-31 12:20 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 10-31 12:20 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-31 12:20 | +15 | BTC | DOWN | 0.67 | open |  |
| 10-31 12:20 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-31 12:20 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-31 12:19 | +10 stop | DOGE | DOWN | 0.67 | 0.42 | -2.83 |
| 10-31 12:19 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-31 12:19 | +5 | DOGE | DOWN | 0.65 | open |  |
| 10-31 12:18 | +10 stop | XRP | DOWN | 0.59 | 0.33 | -2.93 |
| 10-31 12:18 | +15 | XRP | DOWN | 0.58 | open |  |
| 10-31 12:18 | +10 | XRP | DOWN | 0.58 | open |  |
| 10-31 12:17 | +10 stop | BNB | DOWN | 0.62 | 0.45 | -2.05 |
| 10-31 12:17 | +20 | BNB | DOWN | 0.62 | open |  |
| 10-31 12:17 | +15 | BNB | DOWN | 0.62 | open |  |
| 10-31 12:17 | +10 | BNB | DOWN | 0.62 | open |  |
| 10-31 12:17 | +5 | BNB | DOWN | 0.61 | open |  |
| 10-31 12:17 | +10 stop | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 10-31 12:17 | +20 | NEAR | UP | 0.64 | 0.84 | 1.73 |
| 10-31 12:17 | +15 | NEAR | UP | 0.64 | 0.81 | 1.42 |
| 10-31 12:17 | +10 | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 10-31 12:17 | +5 | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 10-31 12:17 | +10 stop | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 10-31 12:17 | +20 | DOGE | DOWN | 0.67 | open |  |
| 10-31 12:17 | +15 | DOGE | DOWN | 0.67 | open |  |
| 10-31 12:17 | +10 | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 10-31 12:17 | +5 | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 10-31 12:17 | +10 stop | ETH | DOWN | 0.66 | open |  |
| 10-31 12:17 | +20 | ETH | DOWN | 0.66 | open |  |
| 10-31 12:17 | +15 | ETH | DOWN | 0.66 | open |  |
| 10-31 12:17 | +10 | ETH | DOWN | 0.66 | open |  |
| 10-31 12:17 | +5 | ETH | DOWN | 0.66 | open |  |
| 10-31 12:16 | +10 stop | HYPE | UP | 0.59 | 0.43 | -1.99 |
| 10-31 12:16 | +20 | HYPE | UP | 0.59 | 0.80 | 1.77 |
| 10-31 12:16 | +15 | HYPE | UP | 0.59 | 0.80 | 1.77 |
| 10-31 12:16 | +10 | HYPE | UP | 0.59 | 0.80 | 1.81 |
| 10-31 12:16 | +5 | HYPE | UP | 0.59 | 0.80 | 1.81 |
| 10-31 12:16 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
