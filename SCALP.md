# Range-Scalp Bot

*Updated Fri Nov 20 01:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65581 | 57248 | 8333 (124) | 4 | $-17547.32 | -4.3% |
| **+10¢** | 48981 | 39239 | 9742 (165) | 6 | $-16299.45 | -5.3% |
| **+15¢** | 41076 | 30567 | 10509 (211) | 6 | $-14667.16 | -5.7% |
| **+20¢** | 36570 | 25529 | 11041 (266) | 6 | $-12986.58 | -5.7% |
| **+10¢ (15¢ stop)** | 79843 | 79679 | 164 (98) | 0 | $-29385.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 01:07 | +5 | BNB | UP | 0.69 | 0.76 | 0.42 |
| 11-20 01:06 | +10 stop | NEAR | DOWN | 0.42 | 0.55 | 0.94 |
| 11-20 01:06 | +10 | NEAR | DOWN | 0.43 | 0.55 | 0.84 |
| 11-20 01:06 | +5 | NEAR | DOWN | 0.43 | 0.55 | 0.84 |
| 11-20 01:06 | +10 stop | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 11-20 01:06 | +10 stop | BNB | DOWN | 0.45 | 0.23 | -2.51 |
| 11-20 01:06 | +15 | BNB | DOWN | 0.45 | open |  |
| 11-20 01:06 | +10 | BNB | DOWN | 0.44 | open |  |
| 11-20 01:06 | +5 | BNB | DOWN | 0.46 | 0.53 | 0.34 |
| 11-20 01:06 | +10 stop | SOL | DOWN | 0.61 | 0.35 | -2.93 |
| 11-20 01:06 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-20 01:06 | +10 | SOL | DOWN | 0.60 | open |  |
| 11-20 01:06 | +5 | SOL | DOWN | 0.62 | 0.69 | 0.38 |
| 11-20 01:05 | +5 | HYPE | DOWN | 0.60 | open |  |
| 11-20 01:05 | +10 stop | BTC | DOWN | 0.59 | 0.43 | -1.95 |
| 11-20 01:05 | +10 stop | ETH | DOWN | 0.67 | 0.42 | -2.84 |
| 11-20 01:05 | +10 stop | XRP | DOWN | 0.69 | 0.48 | -2.43 |
| 11-20 01:05 | +10 | XRP | DOWN | 0.69 | open |  |
| 11-20 01:05 | +5 | XRP | DOWN | 0.69 | open |  |
| 11-20 01:05 | +10 stop | HYPE | DOWN | 0.68 | 0.42 | -2.94 |
| 11-20 01:05 | +10 stop | ETH | UP | 0.52 | 0.62 | 0.65 |
| 11-20 01:05 | +10 stop | ZEC | UP | 0.51 | 0.31 | -2.33 |
| 11-20 01:05 | +10 stop | XRP | UP | 0.50 | 0.61 | 0.75 |
| 11-20 01:05 | +10 | XRP | UP | 0.50 | 0.61 | 0.75 |
| 11-20 01:05 | +5 | XRP | UP | 0.51 | 0.61 | 0.65 |
| 11-20 01:04 | +10 stop | BTC | DOWN | 0.53 | 0.38 | -1.85 |
| 11-20 01:04 | +10 stop | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 11-20 01:04 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-20 01:04 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-20 01:04 | +10 | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 11-20 01:04 | +5 | NEAR | DOWN | 0.70 | 0.79 | 0.63 |
| 11-20 01:03 | +10 stop | SOL | DOWN | 0.61 | 0.75 | 1.09 |
| 11-20 01:03 | +10 stop | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 11-20 01:03 | +5 | BNB | DOWN | 0.59 | 0.66 | 0.37 |
| 11-20 01:03 | +10 stop | XRP | UP | 0.50 | 0.62 | 0.85 |
| 11-20 01:03 | +15 | XRP | UP | 0.50 | 0.72 | 1.87 |
| 11-20 01:03 | +10 | XRP | UP | 0.51 | 0.62 | 0.75 |
| 11-20 01:03 | +5 | XRP | UP | 0.51 | 0.62 | 0.75 |
| 11-20 01:03 | +20 | ZEC | UP | 0.61 | 0.89 | 2.56 |
| 11-20 01:02 | +10 stop | BNB | UP | 0.48 | 0.33 | -1.84 |
