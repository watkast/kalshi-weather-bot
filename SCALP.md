# Range-Scalp Bot

*Updated Thu Nov 05 15:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48456 | 42219 | 6237 (73) | 0 | $-13806.54 | -4.5% |
| **+10¢** | 36175 | 28931 | 7244 (99) | 0 | $-12637.50 | -5.6% |
| **+15¢** | 30310 | 22507 | 7803 (127) | 0 | $-11543.43 | -6.1% |
| **+20¢** | 26929 | 18754 | 8175 (166) | 0 | $-10195.12 | -6.0% |
| **+10¢ (15¢ stop)** | 59061 | 58968 | 93 (56) | 0 | $-21921.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 15:04 | +10 stop | HYPE | UP | 0.57 | 0.34 | -2.64 |
| 11-05 15:04 | +20 | HYPE | UP | 0.57 | no | -5.88 |
| 11-05 15:04 | +15 | HYPE | UP | 0.57 | no | -5.88 |
| 11-05 15:04 | +10 | HYPE | UP | 0.57 | no | -5.88 |
| 11-05 15:04 | +5 | HYPE | UP | 0.57 | no | -5.88 |
| 11-05 15:03 | +10 stop | XRP | DOWN | 0.62 | 0.76 | 1.10 |
| 11-05 15:03 | +10 | XRP | DOWN | 0.64 | 0.76 | 0.95 |
| 11-05 15:03 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-05 15:01 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-05 15:01 | +20 | XRP | DOWN | 0.65 | 0.87 | 1.96 |
| 11-05 15:01 | +15 | XRP | DOWN | 0.65 | 0.87 | 1.96 |
| 11-05 15:01 | +10 | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 11-05 15:01 | +5 | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 11-05 15:01 | +10 stop | SOL | DOWN | 0.66 | 0.77 | 0.82 |
| 11-05 15:01 | +20 | SOL | DOWN | 0.65 | 0.85 | 1.76 |
| 11-05 15:01 | +15 | SOL | DOWN | 0.65 | 0.80 | 1.23 |
| 11-05 15:01 | +10 | SOL | DOWN | 0.65 | 0.77 | 0.92 |
| 11-05 15:01 | +5 | SOL | DOWN | 0.65 | 0.77 | 0.93 |
| 11-05 15:01 | +10 stop | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-05 15:01 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-05 15:01 | +15 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-05 15:01 | +10 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-05 15:01 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 11-05 15:00 | +10 stop | BTC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-05 15:00 | +20 | BTC | DOWN | 0.61 | 0.85 | 2.14 |
| 11-05 15:00 | +15 | BTC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-05 15:00 | +10 | BTC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-05 15:00 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 11-05 15:00 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-05 15:00 | +20 | BNB | DOWN | 0.64 | 0.91 | 2.41 |
| 11-05 15:00 | +15 | BNB | DOWN | 0.64 | 0.81 | 1.42 |
| 11-05 15:00 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.74 |
| 11-05 15:00 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 11-05 14:54 | +5 | BNB | DOWN | 0.58 | 0.65 | 0.36 |
| 11-05 14:54 | +10 stop | BNB | DOWN | 0.56 | 0.79 | 2.01 |
| 11-05 14:54 | +20 | BNB | DOWN | 0.56 | 0.79 | 2.01 |
| 11-05 14:54 | +15 | BNB | DOWN | 0.56 | 0.79 | 2.00 |
| 11-05 14:54 | +10 | BNB | DOWN | 0.56 | 0.79 | 2.00 |
| 11-05 14:54 | +5 | BNB | DOWN | 0.56 | 0.61 | 0.15 |
| 11-05 14:52 | +10 stop | HYPE | DOWN | 0.62 | 0.81 | 1.62 |
