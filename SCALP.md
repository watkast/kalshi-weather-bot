# Range-Scalp Bot

*Updated Tue Nov 03 01:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45391 | 39517 | 5874 (67) | 6 | $-13163.07 | -4.6% |
| **+10¢** | 33881 | 27076 | 6805 (89) | 7 | $-12037.07 | -5.6% |
| **+15¢** | 28338 | 21018 | 7320 (116) | 8 | $-11072.22 | -6.2% |
| **+20¢** | 25167 | 17501 | 7666 (151) | 8 | $-9839.38 | -6.2% |
| **+10¢ (15¢ stop)** | 55394 | 55307 | 87 (51) | 1 | $-20928.38 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 01:04 | +10 stop | ETH | UP | 0.65 | 0.75 | 0.70 |
| 11-03 01:04 | +10 | ETH | UP | 0.65 | 0.75 | 0.70 |
| 11-03 01:04 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 11-03 01:03 | +10 stop | XRP | UP | 0.66 | 0.76 | 0.71 |
| 11-03 01:03 | +5 | XRP | UP | 0.65 | 0.70 | 0.19 |
| 11-03 01:03 | +10 stop | BTC | UP | 0.59 | open |  |
| 11-03 01:03 | +10 stop | BNB | UP | 0.66 | 0.78 | 0.92 |
| 11-03 01:02 | +10 stop | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 11-03 01:02 | +10 stop | ETH | UP | 0.61 | 0.73 | 0.89 |
| 11-03 01:02 | +10 | ETH | UP | 0.61 | 0.73 | 0.89 |
| 11-03 01:02 | +5 | ETH | UP | 0.61 | 0.69 | 0.48 |
| 11-03 01:02 | +10 stop | ETH | DOWN | 0.45 | 0.57 | 0.84 |
| 11-03 01:02 | +20 | ETH | DOWN | 0.45 | open |  |
| 11-03 01:02 | +15 | ETH | DOWN | 0.46 | open |  |
| 11-03 01:02 | +10 | ETH | DOWN | 0.46 | 0.57 | 0.74 |
| 11-03 01:02 | +5 | ETH | DOWN | 0.46 | 0.57 | 0.74 |
| 11-03 01:01 | +10 stop | BNB | DOWN | 0.63 | 0.34 | -3.23 |
| 11-03 01:01 | +20 | BNB | DOWN | 0.63 | open |  |
| 11-03 01:01 | +15 | BNB | DOWN | 0.63 | open |  |
| 11-03 01:01 | +10 | BNB | DOWN | 0.63 | open |  |
| 11-03 01:01 | +5 | BNB | DOWN | 0.63 | open |  |
| 11-03 01:01 | +10 stop | HYPE | DOWN | 0.57 | 0.29 | -3.13 |
| 11-03 01:01 | +20 | HYPE | DOWN | 0.57 | open |  |
| 11-03 01:01 | +15 | HYPE | DOWN | 0.57 | open |  |
| 11-03 01:01 | +10 | HYPE | DOWN | 0.57 | open |  |
| 11-03 01:01 | +5 | HYPE | DOWN | 0.57 | open |  |
| 11-03 01:01 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-03 01:01 | +15 | NEAR | DOWN | 0.67 | open |  |
| 11-03 01:01 | +10 | NEAR | DOWN | 0.65 | open |  |
| 11-03 01:01 | +5 | NEAR | DOWN | 0.65 | open |  |
| 11-03 01:01 | +10 stop | BTC | DOWN | 0.70 | 0.38 | -3.52 |
| 11-03 01:01 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-03 01:01 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-03 01:01 | +10 | BTC | DOWN | 0.70 | open |  |
| 11-03 01:01 | +5 | BTC | DOWN | 0.70 | open |  |
| 11-03 01:01 | +10 stop | XRP | DOWN | 0.62 | 0.46 | -1.95 |
| 11-03 01:01 | +20 | XRP | DOWN | 0.62 | open |  |
| 11-03 01:01 | +15 | XRP | DOWN | 0.62 | open |  |
| 11-03 01:01 | +10 | XRP | DOWN | 0.61 | open |  |
| 11-03 01:01 | +5 | XRP | DOWN | 0.63 | 0.70 | 0.38 |
