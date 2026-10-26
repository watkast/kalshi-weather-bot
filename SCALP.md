# Range-Scalp Bot

*Updated Mon Oct 26 13:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34856 | 30436 | 4420 (43) | 1 | $-9631.02 | -4.4% |
| **+10¢** | 26087 | 20975 | 5112 (65) | 1 | $-8430.93 | -5.1% |
| **+15¢** | 21830 | 16325 | 5505 (89) | 1 | $-7542.82 | -5.5% |
| **+20¢** | 19347 | 13576 | 5771 (112) | 1 | $-6639.76 | -5.5% |
| **+10¢ (15¢ stop)** | 42650 | 42588 | 62 (33) | 0 | $-16172.70 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 13:05 | +10 stop | HYPE | UP | 0.62 | 0.73 | 0.75 |
| 10-26 13:04 | +10 stop | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-26 13:04 | +20 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 10-26 13:04 | +15 | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-26 13:04 | +10 | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-26 13:04 | +5 | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-26 13:04 | +10 stop | ETH | DOWN | 0.68 | 0.86 | 1.55 |
| 10-26 13:04 | +20 | ETH | DOWN | 0.67 | 0.88 | 1.86 |
| 10-26 13:04 | +15 | ETH | DOWN | 0.67 | 0.86 | 1.65 |
| 10-26 13:04 | +10 | ETH | DOWN | 0.67 | 0.86 | 1.65 |
| 10-26 13:04 | +5 | ETH | DOWN | 0.67 | 0.86 | 1.65 |
| 10-26 13:02 | +10 stop | HYPE | DOWN | 0.58 | 0.37 | -2.45 |
| 10-26 13:02 | +20 | HYPE | DOWN | 0.58 | open |  |
| 10-26 13:02 | +15 | HYPE | DOWN | 0.58 | open |  |
| 10-26 13:02 | +10 | HYPE | DOWN | 0.58 | open |  |
| 10-26 13:02 | +5 | HYPE | DOWN | 0.58 | open |  |
| 10-26 13:01 | +10 stop | NEAR | DOWN | 0.57 | 0.71 | 1.07 |
| 10-26 13:01 | +20 | NEAR | DOWN | 0.57 | 0.77 | 1.69 |
| 10-26 13:01 | +15 | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 10-26 13:01 | +10 | NEAR | DOWN | 0.57 | 0.71 | 1.07 |
| 10-26 13:01 | +5 | NEAR | DOWN | 0.57 | 0.71 | 1.07 |
| 10-26 13:00 | +10 stop | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 10-26 13:00 | +20 | BTC | DOWN | 0.65 | 0.87 | 1.96 |
| 10-26 13:00 | +15 | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 10-26 13:00 | +10 | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 10-26 13:00 | +5 | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 10-26 13:00 | +10 stop | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 10-26 13:00 | +20 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 10-26 13:00 | +15 | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 10-26 13:00 | +10 | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 10-26 13:00 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 10-26 12:58 | +10 stop | BTC | DOWN | 0.56 | 0.87 | 2.84 |
| 10-26 12:58 | +15 | BTC | DOWN | 0.56 | 0.87 | 2.84 |
| 10-26 12:58 | +10 | BTC | DOWN | 0.56 | 0.87 | 2.84 |
| 10-26 12:58 | +5 | BTC | DOWN | 0.56 | 0.63 | 0.35 |
| 10-26 12:56 | +5 | BNB | UP | 0.61 | 0.68 | 0.37 |
| 10-26 12:56 | +5 | XRP | UP | 0.71 | 0.78 | 0.42 |
| 10-26 12:55 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-26 12:55 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.92 |
| 10-26 12:55 | +5 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
