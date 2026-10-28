# Range-Scalp Bot

*Updated Wed Oct 28 21:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38527 | 33619 | 4908 (48) | 6 | $-10833.47 | -4.5% |
| **+10¢** | 28733 | 23065 | 5668 (70) | 7 | $-9607.13 | -5.3% |
| **+15¢** | 24036 | 17950 | 6086 (95) | 8 | $-8546.20 | -5.7% |
| **+20¢** | 21323 | 14951 | 6372 (120) | 8 | $-7471.94 | -5.6% |
| **+10¢ (15¢ stop)** | 47124 | 47057 | 67 (35) | 5 | $-17881.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 21:05 | +10 stop | NEAR | UP | 0.71 | 0.55 | -1.93 |
| 10-28 21:05 | +20 | NEAR | UP | 0.71 | open |  |
| 10-28 21:05 | +15 | NEAR | UP | 0.71 | open |  |
| 10-28 21:05 | +10 | NEAR | UP | 0.71 | open |  |
| 10-28 21:05 | +10 stop | BTC | UP | 0.66 | open |  |
| 10-28 21:05 | +5 | BTC | UP | 0.66 | open |  |
| 10-28 21:04 | +5 | ETH | UP | 0.71 | open |  |
| 10-28 21:04 | +10 stop | HYPE | UP | 0.66 | open |  |
| 10-28 21:04 | +10 stop | DOGE | UP | 0.69 | 0.54 | -1.83 |
| 10-28 21:04 | +10 stop | ETH | UP | 0.68 | open |  |
| 10-28 21:04 | +5 | BTC | UP | 0.61 | 0.74 | 0.99 |
| 10-28 21:03 | +10 stop | SOL | UP | 0.63 | open |  |
| 10-28 21:03 | +10 stop | ZEC | UP | 0.68 | open |  |
| 10-28 21:03 | +20 | ZEC | UP | 0.68 | open |  |
| 10-28 21:03 | +15 | ZEC | UP | 0.68 | open |  |
| 10-28 21:03 | +10 | ZEC | UP | 0.68 | open |  |
| 10-28 21:03 | +5 | ZEC | UP | 0.68 | 0.74 | 0.30 |
| 10-28 21:03 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-28 21:03 | +20 | XRP | DOWN | 0.56 | open |  |
| 10-28 21:03 | +15 | XRP | DOWN | 0.57 | open |  |
| 10-28 21:03 | +10 | XRP | DOWN | 0.57 | 0.67 | 0.66 |
| 10-28 21:03 | +5 | XRP | DOWN | 0.57 | 0.67 | 0.66 |
| 10-28 21:03 | +5 | BTC | DOWN | 0.49 | 0.57 | 0.44 |
| 10-28 21:03 | +5 | BNB | UP | 0.65 | 0.73 | 0.50 |
| 10-28 21:02 | +5 | NEAR | DOWN | 0.58 | open |  |
| 10-28 21:02 | +5 | NEAR | DOWN | 0.47 | 0.57 | 0.64 |
| 10-28 21:02 | +10 stop | DOGE | DOWN | 0.62 | 0.44 | -2.20 |
| 10-28 21:02 | +10 | DOGE | DOWN | 0.63 | open |  |
| 10-28 21:02 | +10 stop | HYPE | DOWN | 0.65 | 0.47 | -2.14 |
| 10-28 21:02 | +20 | HYPE | DOWN | 0.65 | open |  |
| 10-28 21:02 | +15 | HYPE | DOWN | 0.65 | open |  |
| 10-28 21:02 | +10 | HYPE | DOWN | 0.65 | open |  |
| 10-28 21:02 | +5 | HYPE | DOWN | 0.65 | open |  |
| 10-28 21:02 | +10 stop | SOL | DOWN | 0.66 | 0.44 | -2.54 |
| 10-28 21:02 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-28 21:01 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-28 21:01 | +10 stop | BNB | UP | 0.56 | 0.73 | 1.38 |
| 10-28 21:01 | +20 | BNB | UP | 0.56 | 0.79 | 2.00 |
| 10-28 21:01 | +15 | BNB | UP | 0.56 | 0.73 | 1.38 |
| 10-28 21:01 | +10 | BNB | UP | 0.56 | 0.73 | 1.38 |
