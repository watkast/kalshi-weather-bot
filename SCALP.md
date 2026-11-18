# Range-Scalp Bot

*Updated Wed Nov 18 23:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64432 | 56203 | 8229 (124) | 1 | $-17539.97 | -4.3% |
| **+10¢** | 48134 | 38510 | 9624 (165) | 2 | $-16353.08 | -5.4% |
| **+15¢** | 40356 | 29984 | 10372 (210) | 4 | $-14767.51 | -5.8% |
| **+20¢** | 35934 | 25046 | 10888 (265) | 5 | $-13061.66 | -5.8% |
| **+10¢ (15¢ stop)** | 78378 | 78214 | 164 (98) | 1 | $-28846.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 23:23 | +10 stop | ZEC | UP | 0.62 | open |  |
| 11-18 23:23 | +20 | ZEC | UP | 0.62 | open |  |
| 11-18 23:23 | +15 | ZEC | UP | 0.62 | open |  |
| 11-18 23:23 | +10 | ZEC | UP | 0.62 | open |  |
| 11-18 23:23 | +5 | ZEC | UP | 0.61 | 0.71 | 0.68 |
| 11-18 23:22 | +10 stop | ZEC | DOWN | 0.44 | 0.68 | 2.06 |
| 11-18 23:22 | +20 | ZEC | DOWN | 0.44 | 0.68 | 2.06 |
| 11-18 23:22 | +15 | ZEC | DOWN | 0.44 | 0.68 | 2.06 |
| 11-18 23:22 | +10 | ZEC | DOWN | 0.44 | 0.68 | 2.06 |
| 11-18 23:22 | +5 | ZEC | DOWN | 0.44 | 0.68 | 2.07 |
| 11-18 23:21 | +10 stop | SOL | DOWN | 0.43 | 0.57 | 1.04 |
| 11-18 23:21 | +10 | SOL | DOWN | 0.43 | 0.57 | 1.04 |
| 11-18 23:21 | +5 | SOL | DOWN | 0.43 | 0.57 | 1.04 |
| 11-18 23:21 | +10 stop | ETH | DOWN | 0.50 | 0.17 | -3.58 |
| 11-18 23:21 | +5 | ETH | DOWN | 0.50 | 0.56 | 0.24 |
| 11-18 23:19 | +10 stop | BTC | DOWN | 0.67 | 0.42 | -2.84 |
| 11-18 23:19 | +5 | BTC | DOWN | 0.67 | open |  |
| 11-18 23:18 | +10 stop | HYPE | DOWN | 0.52 | 0.62 | 0.65 |
| 11-18 23:18 | +15 | HYPE | DOWN | 0.52 | 0.73 | 1.78 |
| 11-18 23:18 | +10 | HYPE | DOWN | 0.52 | 0.62 | 0.65 |
| 11-18 23:18 | +5 | HYPE | DOWN | 0.52 | 0.62 | 0.65 |
| 11-18 23:18 | +10 stop | NEAR | DOWN | 0.55 | 0.73 | 1.45 |
| 11-18 23:18 | +15 | NEAR | DOWN | 0.55 | 0.73 | 1.45 |
| 11-18 23:18 | +10 | NEAR | DOWN | 0.55 | 0.73 | 1.45 |
| 11-18 23:18 | +5 | NEAR | DOWN | 0.55 | 0.63 | 0.45 |
| 11-18 23:18 | +10 stop | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 11-18 23:18 | +15 | XRP | DOWN | 0.61 | 0.79 | 1.51 |
| 11-18 23:18 | +10 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 11-18 23:18 | +5 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 11-18 23:18 | +5 | BNB | DOWN | 0.59 | 0.67 | 0.51 |
| 11-18 23:17 | +10 stop | SOL | DOWN | 0.70 | 0.49 | -2.43 |
| 11-18 23:17 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-18 23:17 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-18 23:17 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-18 23:17 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 11-18 23:17 | +10 stop | BNB | DOWN | 0.63 | 0.45 | -2.15 |
| 11-18 23:17 | +20 | BNB | DOWN | 0.62 | open |  |
| 11-18 23:17 | +15 | BNB | DOWN | 0.62 | open |  |
| 11-18 23:17 | +10 | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 11-18 23:17 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
