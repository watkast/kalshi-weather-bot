# Range-Scalp Bot

*Updated Fri Nov 13 00:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57488 | 50132 | 7356 (101) | 4 | $-15702.34 | -4.3% |
| **+10¢** | 42973 | 34384 | 8589 (133) | 5 | $-14633.97 | -5.4% |
| **+15¢** | 36027 | 26783 | 9244 (167) | 6 | $-13199.23 | -5.8% |
| **+20¢** | 32097 | 22399 | 9698 (217) | 8 | $-11548.01 | -5.7% |
| **+10¢ (15¢ stop)** | 70101 | 69973 | 128 (78) | 2 | $-25829.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 00:05 | +10 stop | BTC | UP | 0.65 | open |  |
| 11-13 00:04 | +10 stop | HYPE | UP | 0.54 | open |  |
| 11-13 00:04 | +20 | HYPE | UP | 0.54 | open |  |
| 11-13 00:04 | +15 | HYPE | UP | 0.54 | open |  |
| 11-13 00:04 | +10 | HYPE | UP | 0.53 | open |  |
| 11-13 00:04 | +5 | HYPE | UP | 0.53 | open |  |
| 11-13 00:04 | +10 stop | BTC | UP | 0.71 | 0.56 | -1.83 |
| 11-13 00:04 | +15 | BTC | UP | 0.71 | open |  |
| 11-13 00:04 | +10 | BTC | UP | 0.71 | open |  |
| 11-13 00:04 | +10 stop | SOL | UP | 0.65 | 0.49 | -1.94 |
| 11-13 00:04 | +10 | SOL | UP | 0.65 | open |  |
| 11-13 00:04 | +5 | SOL | UP | 0.65 | open |  |
| 11-13 00:04 | +5 | BTC | UP | 0.71 | open |  |
| 11-13 00:04 | +10 stop | ETH | UP | 0.64 | 0.49 | -1.85 |
| 11-13 00:04 | +20 | ETH | UP | 0.64 | open |  |
| 11-13 00:04 | +15 | ETH | UP | 0.64 | open |  |
| 11-13 00:04 | +10 | ETH | UP | 0.64 | open |  |
| 11-13 00:04 | +5 | ETH | UP | 0.64 | open |  |
| 11-13 00:03 | +10 stop | NEAR | UP | 0.57 | 0.70 | 0.97 |
| 11-13 00:03 | +20 | NEAR | UP | 0.57 | open |  |
| 11-13 00:03 | +15 | NEAR | UP | 0.57 | open |  |
| 11-13 00:03 | +10 | NEAR | UP | 0.57 | 0.70 | 0.97 |
| 11-13 00:03 | +5 | NEAR | UP | 0.57 | 0.62 | 0.15 |
| 11-13 00:03 | +5 | BTC | UP | 0.46 | 0.55 | 0.54 |
| 11-13 00:02 | +10 stop | SOL | UP | 0.53 | 0.68 | 1.12 |
| 11-13 00:02 | +20 | SOL | UP | 0.54 | open |  |
| 11-13 00:02 | +15 | SOL | UP | 0.54 | open |  |
| 11-13 00:02 | +10 | SOL | UP | 0.55 | 0.68 | 0.96 |
| 11-13 00:02 | +5 | SOL | UP | 0.55 | 0.68 | 0.96 |
| 11-13 00:02 | +10 stop | BTC | UP | 0.52 | 0.68 | 1.26 |
| 11-13 00:02 | +20 | BTC | UP | 0.52 | open |  |
| 11-13 00:02 | +15 | BTC | UP | 0.52 | 0.68 | 1.26 |
| 11-13 00:02 | +10 | BTC | UP | 0.52 | 0.68 | 1.26 |
| 11-13 00:02 | +5 | BTC | UP | 0.52 | 0.58 | 0.24 |
| 11-13 00:01 | +10 stop | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-13 00:01 | +20 | BNB | UP | 0.71 | open |  |
| 11-13 00:01 | +15 | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-13 00:01 | +10 | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-13 00:01 | +5 | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-13 00:01 | +10 stop | ZEC | UP | 0.67 | 0.52 | -1.84 |
