# Range-Scalp Bot

*Updated Thu Nov 12 23:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57433 | 50083 | 7350 (101) | 3 | $-15687.09 | -4.3% |
| **+10¢** | 42930 | 34348 | 8582 (133) | 3 | $-14629.10 | -5.4% |
| **+15¢** | 35994 | 26758 | 9236 (167) | 3 | $-13190.15 | -5.8% |
| **+20¢** | 32070 | 22380 | 9690 (217) | 3 | $-11538.81 | -5.7% |
| **+10¢ (15¢ stop)** | 70048 | 69920 | 128 (78) | 0 | $-25839.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 23:05 | +10 stop | XRP | UP | 0.65 | 0.75 | 0.70 |
| 11-12 23:05 | +10 | XRP | UP | 0.65 | 0.75 | 0.70 |
| 11-12 23:05 | +5 | XRP | UP | 0.65 | 0.75 | 0.70 |
| 11-12 23:05 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-12 23:03 | +15 | SOL | UP | 0.69 | 0.85 | 1.36 |
| 11-12 23:03 | +10 | SOL | UP | 0.69 | 0.81 | 0.94 |
| 11-12 23:03 | +10 stop | SOL | UP | 0.70 | 0.81 | 0.84 |
| 11-12 23:03 | +5 | ETH | UP | 0.66 | 0.73 | 0.40 |
| 11-12 23:03 | +10 stop | BTC | UP | 0.57 | 0.74 | 1.38 |
| 11-12 23:03 | +10 stop | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 11-12 23:03 | +20 | HYPE | UP | 0.69 | 0.92 | 2.10 |
| 11-12 23:03 | +15 | HYPE | UP | 0.69 | 0.87 | 1.57 |
| 11-12 23:03 | +10 | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 11-12 23:03 | +5 | HYPE | UP | 0.69 | 0.75 | 0.31 |
| 11-12 23:03 | +20 | SOL | UP | 0.71 | 0.92 | 1.91 |
| 11-12 23:03 | +5 | SOL | UP | 0.71 | 0.78 | 0.42 |
| 11-12 23:01 | +10 stop | ETH | UP | 0.69 | 0.84 | 1.25 |
| 11-12 23:01 | +20 | ETH | UP | 0.68 | 0.89 | 1.87 |
| 11-12 23:01 | +15 | ETH | UP | 0.70 | 0.89 | 1.68 |
| 11-12 23:01 | +10 | ETH | UP | 0.70 | 0.84 | 1.15 |
| 11-12 23:01 | +5 | ETH | UP | 0.70 | 0.77 | 0.42 |
| 11-12 23:01 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 11-12 23:01 | +10 stop | BTC | DOWN | 0.56 | 0.28 | -3.13 |
| 11-12 23:01 | +20 | BTC | DOWN | 0.56 | open |  |
| 11-12 23:01 | +15 | BTC | DOWN | 0.56 | open |  |
| 11-12 23:01 | +10 | BTC | DOWN | 0.56 | open |  |
| 11-12 23:01 | +5 | BTC | DOWN | 0.56 | open |  |
| 11-12 23:01 | +10 stop | XRP | UP | 0.68 | 0.80 | 0.93 |
| 11-12 23:01 | +20 | XRP | UP | 0.68 | 0.88 | 1.77 |
| 11-12 23:01 | +15 | XRP | UP | 0.68 | 0.85 | 1.46 |
| 11-12 23:01 | +10 | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-12 23:01 | +5 | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-12 23:00 | +10 stop | BNB | DOWN | 0.68 | 0.49 | -2.24 |
| 11-12 23:00 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-12 23:00 | +15 | BNB | DOWN | 0.68 | open |  |
| 11-12 23:00 | +10 | BNB | DOWN | 0.68 | open |  |
| 11-12 23:00 | +5 | BNB | DOWN | 0.68 | open |  |
| 11-12 23:00 | +10 stop | DOGE | DOWN | 0.63 | 0.46 | -2.05 |
| 11-12 23:00 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-12 23:00 | +15 | DOGE | DOWN | 0.63 | open |  |
