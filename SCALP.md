# Range-Scalp Bot

*Updated Sat Oct 31 14:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42312 | 36905 | 5407 (58) | 2 | $-11924.30 | -4.5% |
| **+10¢** | 31547 | 25287 | 6260 (81) | 3 | $-10715.17 | -5.4% |
| **+15¢** | 26381 | 19632 | 6749 (109) | 6 | $-9810.55 | -5.9% |
| **+20¢** | 23431 | 16361 | 7070 (141) | 6 | $-8657.14 | -5.9% |
| **+10¢ (15¢ stop)** | 51602 | 51523 | 79 (44) | 0 | $-19502.73 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 14:05 | +20 | XRP | DOWN | 0.70 | open |  |
| 10-31 14:04 | +10 stop | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-31 14:04 | +20 | BTC | UP | 0.71 | open |  |
| 10-31 14:04 | +15 | BTC | UP | 0.71 | open |  |
| 10-31 14:04 | +10 | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-31 14:04 | +10 stop | ETH | UP | 0.58 | 0.42 | -1.96 |
| 10-31 14:04 | +15 | XRP | DOWN | 0.68 | open |  |
| 10-31 14:04 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-31 14:04 | +10 stop | XRP | DOWN | 0.68 | 0.44 | -2.74 |
| 10-31 14:04 | +10 | XRP | DOWN | 0.68 | open |  |
| 10-31 14:04 | +5 | XRP | DOWN | 0.68 | 0.76 | 0.51 |
| 10-31 14:03 | +10 stop | XRP | DOWN | 0.44 | 0.59 | 1.15 |
| 10-31 14:03 | +20 | XRP | DOWN | 0.44 | 0.67 | 1.96 |
| 10-31 14:03 | +15 | XRP | DOWN | 0.45 | 0.63 | 1.45 |
| 10-31 14:03 | +10 | XRP | DOWN | 0.45 | 0.59 | 1.05 |
| 10-31 14:03 | +5 | XRP | DOWN | 0.45 | 0.59 | 1.05 |
| 10-31 14:03 | +5 | NEAR | DOWN | 0.49 | 0.65 | 1.26 |
| 10-31 14:03 | +10 stop | BTC | DOWN | 0.71 | 0.52 | -2.23 |
| 10-31 14:02 | +5 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-31 14:02 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-31 14:02 | +10 stop | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-31 14:02 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-31 14:02 | +15 | SOL | DOWN | 0.66 | open |  |
| 10-31 14:02 | +10 | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-31 14:02 | +5 | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-31 14:02 | +10 stop | NEAR | DOWN | 0.63 | 0.48 | -1.85 |
| 10-31 14:02 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-31 14:02 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-31 14:02 | +10 | NEAR | DOWN | 0.63 | open |  |
| 10-31 14:02 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.28 |
| 10-31 14:01 | +10 stop | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-31 14:01 | +20 | HYPE | DOWN | 0.62 | 0.84 | 1.93 |
| 10-31 14:01 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-31 14:01 | +10 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-31 14:01 | +5 | HYPE | DOWN | 0.62 | 0.67 | 0.17 |
| 10-31 14:01 | +10 stop | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 10-31 14:01 | +20 | BNB | DOWN | 0.65 | 0.85 | 1.75 |
| 10-31 14:01 | +15 | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 10-31 14:01 | +10 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 10-31 14:01 | +5 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
