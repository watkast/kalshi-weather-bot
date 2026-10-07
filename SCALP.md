# Range-Scalp Bot

*Updated Wed Oct 07 14:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6537 | 5678 | 859 (9) | 4 | $-1961.85 | -4.8% |
| **+10¢** | 4963 | 3955 | 1008 (16) | 4 | $-1839.14 | -5.9% |
| **+15¢** | 4164 | 3099 | 1065 (20) | 6 | $-1551.76 | -5.9% |
| **+20¢** | 3720 | 2606 | 1114 (27) | 8 | $-1268.72 | -5.4% |
| **+10¢ (15¢ stop)** | 7929 | 7914 | 15 (9) | 3 | $-2803.81 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 14:08 | +10 stop | BTC | DOWN | 0.43 | 0.54 | 0.74 |
| 10-07 14:08 | +10 | BTC | DOWN | 0.43 | 0.54 | 0.74 |
| 10-07 14:08 | +5 | BTC | DOWN | 0.43 | 0.54 | 0.74 |
| 10-07 14:08 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-07 14:08 | +10 stop | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 10-07 14:08 | +20 | NEAR | DOWN | 0.58 | open |  |
| 10-07 14:08 | +15 | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 10-07 14:08 | +10 | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 10-07 14:08 | +5 | NEAR | DOWN | 0.58 | 0.64 | 0.25 |
| 10-07 14:08 | +10 stop | SOL | DOWN | 0.62 | open |  |
| 10-07 14:08 | +5 | SOL | DOWN | 0.62 | open |  |
| 10-07 14:08 | +10 stop | XRP | DOWN | 0.52 | 0.64 | 0.86 |
| 10-07 14:08 | +15 | XRP | DOWN | 0.52 | open |  |
| 10-07 14:08 | +10 | XRP | DOWN | 0.51 | 0.64 | 0.95 |
| 10-07 14:08 | +5 | XRP | DOWN | 0.51 | 0.64 | 0.95 |
| 10-07 14:07 | +10 stop | ZEC | UP | 0.63 | open |  |
| 10-07 14:07 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-07 14:07 | +15 | BNB | DOWN | 0.70 | open |  |
| 10-07 14:07 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-07 14:07 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-07 14:07 | +10 stop | SOL | DOWN | 0.49 | 0.59 | 0.65 |
| 10-07 14:07 | +10 | SOL | DOWN | 0.49 | 0.66 | 1.33 |
| 10-07 14:07 | +5 | SOL | DOWN | 0.47 | 0.59 | 0.85 |
| 10-07 14:07 | +20 | ZEC | DOWN | 0.54 | open |  |
| 10-07 14:07 | +15 | ZEC | DOWN | 0.54 | open |  |
| 10-07 14:07 | +10 | ZEC | DOWN | 0.54 | open |  |
| 10-07 14:07 | +5 | ZEC | DOWN | 0.55 | open |  |
| 10-07 14:06 | +10 stop | HYPE | DOWN | 0.62 | 0.46 | -1.95 |
| 10-07 14:06 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-07 14:06 | +15 | HYPE | DOWN | 0.62 | open |  |
| 10-07 14:06 | +10 | HYPE | DOWN | 0.62 | open |  |
| 10-07 14:06 | +5 | HYPE | DOWN | 0.62 | open |  |
| 10-07 14:05 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-07 14:05 | +10 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-07 14:05 | +5 | SOL | DOWN | 0.61 | 0.70 | 0.58 |
| 10-07 14:05 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-07 14:05 | +10 stop | ZEC | DOWN | 0.65 | 0.50 | -1.84 |
| 10-07 14:04 | +10 stop | BTC | DOWN | 0.70 | 0.55 | -1.83 |
| 10-07 14:03 | +5 | ETH | DOWN | 0.65 | 0.73 | 0.50 |
| 10-07 14:03 | +5 | BTC | DOWN | 0.60 | 0.69 | 0.62 |
