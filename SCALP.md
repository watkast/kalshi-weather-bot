# Range-Scalp Bot

*Updated Mon Oct 19 06:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23560 | 20488 | 3072 (30) | 2 | $-7014.14 | -4.7% |
| **+10¢** | 17721 | 14181 | 3540 (44) | 2 | $-6251.54 | -5.6% |
| **+15¢** | 14850 | 11035 | 3815 (66) | 5 | $-5671.56 | -6.1% |
| **+20¢** | 13147 | 9156 | 3991 (85) | 5 | $-5028.53 | -6.1% |
| **+10¢ (15¢ stop)** | 29024 | 28973 | 51 (30) | 1 | $-11000.35 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 06:08 | +10 stop | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 10-19 06:08 | +10 | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 10-19 06:08 | +5 | DOGE | UP | 0.54 | 0.62 | 0.45 |
| 10-19 06:07 | +10 stop | DOGE | UP | 0.62 | 0.74 | 0.89 |
| 10-19 06:07 | +5 | DOGE | UP | 0.62 | 0.74 | 0.89 |
| 10-19 06:07 | +5 | HYPE | UP | 0.59 | 0.73 | 1.09 |
| 10-19 06:07 | +10 stop | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-19 06:07 | +10 | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-19 06:07 | +5 | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-19 06:06 | +10 stop | BNB | UP | 0.71 | open |  |
| 10-19 06:06 | +5 | BNB | UP | 0.71 | open |  |
| 10-19 06:05 | +10 stop | XRP | UP | 0.56 | 0.76 | 1.69 |
| 10-19 06:05 | +5 | XRP | UP | 0.56 | 0.64 | 0.45 |
| 10-19 06:05 | +10 stop | DOGE | DOWN | 0.49 | 0.61 | 0.85 |
| 10-19 06:05 | +10 stop | BTC | UP | 0.69 | 0.81 | 0.94 |
| 10-19 06:05 | +15 | BTC | UP | 0.69 | 0.85 | 1.36 |
| 10-19 06:05 | +10 | BTC | UP | 0.69 | 0.81 | 0.94 |
| 10-19 06:05 | +5 | BTC | UP | 0.69 | 0.77 | 0.52 |
| 10-19 06:05 | +5 | NEAR | UP | 0.62 | 0.70 | 0.48 |
| 10-19 06:05 | +10 stop | BNB | UP | 0.50 | 0.64 | 1.05 |
| 10-19 06:04 | +10 stop | HYPE | UP | 0.66 | 0.84 | 1.54 |
| 10-19 06:04 | +10 | HYPE | UP | 0.66 | 0.84 | 1.54 |
| 10-19 06:04 | +5 | HYPE | UP | 0.66 | 0.72 | 0.29 |
| 10-19 06:04 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-19 06:04 | +10 stop | ETH | UP | 0.71 | 0.56 | -1.83 |
| 10-19 06:04 | +10 | ETH | UP | 0.71 | 0.85 | 1.16 |
| 10-19 06:04 | +5 | ETH | UP | 0.71 | 0.85 | 1.16 |
| 10-19 06:03 | +5 | BNB | UP | 0.59 | 0.64 | 0.16 |
| 10-19 06:03 | +10 stop | SOL | UP | 0.64 | 0.84 | 1.73 |
| 10-19 06:03 | +10 | SOL | UP | 0.64 | 0.84 | 1.73 |
| 10-19 06:03 | +5 | SOL | UP | 0.64 | 0.70 | 0.28 |
| 10-19 06:03 | +5 | DOGE | UP | 0.59 | 0.71 | 0.88 |
| 10-19 06:03 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 10-19 06:03 | +5 | HYPE | UP | 0.66 | 0.71 | 0.19 |
| 10-19 06:02 | +10 stop | BNB | UP | 0.66 | 0.49 | -2.04 |
| 10-19 06:02 | +20 | BNB | UP | 0.66 | open |  |
| 10-19 06:02 | +15 | BNB | UP | 0.67 | open |  |
| 10-19 06:02 | +10 | BNB | UP | 0.67 | open |  |
| 10-19 06:02 | +5 | BNB | UP | 0.67 | 0.73 | 0.30 |
| 10-19 06:02 | +10 stop | DOGE | UP | 0.63 | 0.35 | -3.17 |
