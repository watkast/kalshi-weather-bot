# Range-Scalp Bot

*Updated Tue Nov 24 07:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70577 | 61603 | 8974 (148) | 2 | $-18869.16 | -4.2% |
| **+10¢** | 52648 | 42171 | 10477 (192) | 2 | $-17469.32 | -5.3% |
| **+15¢** | 44106 | 32822 | 11284 (248) | 2 | $-15535.90 | -5.6% |
| **+20¢** | 39279 | 27400 | 11879 (314) | 2 | $-13886.87 | -5.6% |
| **+10¢ (15¢ stop)** | 85941 | 85743 | 198 (118) | 0 | $-31597.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 07:11 | +10 stop | HYPE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-24 07:11 | +5 | HYPE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-24 07:10 | +10 stop | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-24 07:09 | +10 stop | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 11-24 07:09 | +10 stop | BTC | UP | 0.56 | 0.37 | -2.25 |
| 11-24 07:09 | +5 | BTC | UP | 0.56 | open |  |
| 11-24 07:09 | +10 stop | HYPE | UP | 0.58 | 0.41 | -2.05 |
| 11-24 07:09 | +10 stop | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 11-24 07:09 | +10 stop | ETH | UP | 0.42 | 0.55 | 0.94 |
| 11-24 07:08 | +10 stop | SOL | UP | 0.51 | 0.61 | 0.65 |
| 11-24 07:08 | +10 stop | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 11-24 07:07 | +10 stop | ETH | DOWN | 0.59 | 0.38 | -2.44 |
| 11-24 07:06 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.22 |
| 11-24 07:06 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.36 |
| 11-24 07:05 | +10 stop | SOL | DOWN | 0.59 | 0.41 | -2.14 |
| 11-24 07:05 | +10 stop | BTC | UP | 0.59 | 0.73 | 1.09 |
| 11-24 07:04 | +10 stop | BNB | DOWN | 0.51 | 0.69 | 1.47 |
| 11-24 07:04 | +20 | BNB | DOWN | 0.53 | 0.85 | 2.93 |
| 11-24 07:04 | +15 | BNB | DOWN | 0.53 | 0.69 | 1.27 |
| 11-24 07:04 | +10 | BNB | DOWN | 0.53 | 0.69 | 1.27 |
| 11-24 07:04 | +5 | BNB | DOWN | 0.53 | 0.59 | 0.25 |
| 11-24 07:03 | +10 stop | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 11-24 07:03 | +5 | ETH | DOWN | 0.59 | 0.65 | 0.27 |
| 11-24 07:03 | +10 stop | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-24 07:03 | +10 stop | BTC | UP | 0.50 | 0.62 | 0.85 |
| 11-24 07:03 | +10 stop | HYPE | UP | 0.58 | 0.72 | 1.07 |
| 11-24 07:03 | +5 | BTC | UP | 0.62 | 0.73 | 0.79 |
| 11-24 07:03 | +10 stop | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-24 07:03 | +20 | DOGE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-24 07:03 | +15 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-24 07:03 | +10 | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-24 07:03 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 11-24 07:02 | +10 stop | BTC | DOWN | 0.59 | 0.42 | -2.05 |
| 11-24 07:02 | +20 | BTC | DOWN | 0.58 | 0.90 | 2.98 |
| 11-24 07:02 | +15 | BTC | DOWN | 0.58 | 0.77 | 1.59 |
| 11-24 07:02 | +10 | BTC | DOWN | 0.59 | 0.77 | 1.50 |
| 11-24 07:02 | +5 | BTC | DOWN | 0.59 | 0.68 | 0.57 |
| 11-24 07:02 | +5 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-24 07:01 | +10 stop | NEAR | DOWN | 0.60 | 0.32 | -3.17 |
| 11-24 07:01 | +20 | NEAR | DOWN | 0.60 | open |  |
