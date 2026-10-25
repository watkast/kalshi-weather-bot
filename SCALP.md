# Range-Scalp Bot

*Updated Sun Oct 25 18:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33531 | 29261 | 4270 (43) | 2 | $-9376.23 | -4.4% |
| **+10¢** | 25097 | 20153 | 4944 (65) | 2 | $-8302.71 | -5.3% |
| **+15¢** | 20993 | 15671 | 5322 (89) | 0 | $-7450.76 | -5.7% |
| **+20¢** | 18604 | 13032 | 5572 (111) | 2 | $-6554.26 | -5.6% |
| **+10¢ (15¢ stop)** | 41093 | 41031 | 62 (33) | 1 | $-15669.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 18:09 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 10-25 18:09 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-25 18:09 | +10 stop | HYPE | DOWN | 0.50 | 0.60 | 0.65 |
| 10-25 18:09 | +15 | HYPE | DOWN | 0.50 | 0.65 | 1.16 |
| 10-25 18:09 | +10 | HYPE | DOWN | 0.50 | 0.60 | 0.65 |
| 10-25 18:07 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-25 18:07 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-25 18:07 | +5 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 18:06 | +10 stop | BNB | DOWN | 0.57 | 0.71 | 1.07 |
| 10-25 18:06 | +20 | BNB | DOWN | 0.57 | 0.81 | 2.11 |
| 10-25 18:06 | +15 | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 10-25 18:06 | +10 | BNB | DOWN | 0.58 | 0.71 | 0.97 |
| 10-25 18:06 | +5 | BNB | DOWN | 0.58 | 0.71 | 0.97 |
| 10-25 18:06 | +5 | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 10-25 18:05 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-25 18:05 | +5 | NEAR | DOWN | 0.58 | 0.64 | 0.25 |
| 10-25 18:05 | +5 | HYPE | UP | 0.60 | open |  |
| 10-25 18:04 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-25 18:04 | +10 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-25 18:04 | +5 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-25 18:04 | +10 stop | NEAR | DOWN | 0.60 | 0.78 | 1.50 |
| 10-25 18:04 | +20 | NEAR | DOWN | 0.60 | 0.81 | 1.82 |
| 10-25 18:04 | +15 | NEAR | DOWN | 0.60 | 0.78 | 1.50 |
| 10-25 18:04 | +10 | NEAR | DOWN | 0.60 | 0.78 | 1.50 |
| 10-25 18:04 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.27 |
| 10-25 18:04 | +10 stop | BTC | UP | 0.61 | 0.30 | -3.42 |
| 10-25 18:04 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-25 18:02 | +10 stop | DOGE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-25 18:02 | +10 stop | HYPE | UP | 0.52 | 0.28 | -2.73 |
| 10-25 18:02 | +5 | HYPE | UP | 0.54 | 0.59 | 0.15 |
| 10-25 18:02 | +10 stop | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 10-25 18:02 | +20 | XRP | DOWN | 0.68 | 0.89 | 1.87 |
| 10-25 18:02 | +15 | XRP | DOWN | 0.68 | 0.87 | 1.66 |
| 10-25 18:02 | +10 | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 10-25 18:02 | +5 | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 10-25 18:02 | +10 stop | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 10-25 18:02 | +20 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 10-25 18:02 | +15 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-25 18:02 | +10 | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 10-25 18:02 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
