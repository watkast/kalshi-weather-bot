# Range-Scalp Bot

*Updated Sun Nov 15 13:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60810 | 53052 | 7758 (112) | 2 | $-16462.60 | -4.3% |
| **+10¢** | 45432 | 36336 | 9096 (150) | 2 | $-15532.60 | -5.4% |
| **+15¢** | 38053 | 28242 | 9811 (188) | 2 | $-14207.53 | -6.0% |
| **+20¢** | 33910 | 23619 | 10291 (240) | 3 | $-12501.57 | -5.9% |
| **+10¢ (15¢ stop)** | 74010 | 73859 | 151 (89) | 1 | $-27206.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 13:11 | +10 stop | ETH | UP | 0.56 | open |  |
| 11-15 13:10 | +10 stop | ETH | DOWN | 0.65 | 0.37 | -3.13 |
| 11-15 13:10 | +20 | ETH | DOWN | 0.65 | open |  |
| 11-15 13:10 | +15 | ETH | DOWN | 0.66 | open |  |
| 11-15 13:10 | +10 | ETH | DOWN | 0.66 | open |  |
| 11-15 13:10 | +5 | ETH | DOWN | 0.66 | open |  |
| 11-15 13:09 | +10 stop | BTC | UP | 0.66 | 0.81 | 1.23 |
| 11-15 13:09 | +10 stop | BNB | DOWN | 0.63 | 0.35 | -3.13 |
| 11-15 13:09 | +10 stop | DOGE | DOWN | 0.47 | 0.15 | -3.47 |
| 11-15 13:08 | +10 stop | BTC | DOWN | 0.63 | 0.42 | -2.45 |
| 11-15 13:07 | +10 stop | SOL | UP | 0.51 | 0.66 | 1.16 |
| 11-15 13:06 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-15 13:06 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-15 13:06 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.85 |
| 11-15 13:06 | +15 | NEAR | DOWN | 0.71 | 0.86 | 1.26 |
| 11-15 13:06 | +10 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-15 13:06 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 11-15 13:06 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-15 13:06 | +10 stop | BTC | UP | 0.61 | 0.35 | -2.93 |
| 11-15 13:06 | +10 | BTC | UP | 0.61 | 0.81 | 1.72 |
| 11-15 13:06 | +5 | BTC | UP | 0.61 | 0.81 | 1.72 |
| 11-15 13:05 | +10 stop | BNB | UP | 0.55 | 0.37 | -2.15 |
| 11-15 13:05 | +10 stop | DOGE | DOWN | 0.57 | 0.70 | 0.97 |
| 11-15 13:04 | +10 stop | HYPE | DOWN | 0.65 | 0.39 | -2.93 |
| 11-15 13:04 | +5 | BTC | UP | 0.60 | 0.67 | 0.37 |
| 11-15 13:03 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-15 13:03 | +20 | ETH | DOWN | 0.68 | 0.91 | 2.09 |
| 11-15 13:03 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-15 13:03 | +10 stop | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 11-15 13:03 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-15 13:03 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 11-15 13:02 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-15 13:02 | +20 | ZEC | DOWN | 0.58 | 0.81 | 2.01 |
| 11-15 13:02 | +15 | ZEC | DOWN | 0.58 | 0.74 | 1.28 |
| 11-15 13:02 | +10 | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-15 13:02 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
| 11-15 13:02 | +10 stop | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
| 11-15 13:02 | +20 | NEAR | DOWN | 0.59 | 0.79 | 1.71 |
| 11-15 13:02 | +15 | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 11-15 13:02 | +10 | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
