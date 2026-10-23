# Range-Scalp Bot

*Updated Fri Oct 23 07:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29957 | 26082 | 3875 (39) | 1 | $-8802.56 | -4.7% |
| **+10¢** | 22461 | 17975 | 4486 (55) | 1 | $-7904.47 | -5.6% |
| **+15¢** | 18807 | 13985 | 4822 (78) | 1 | $-7117.96 | -6.0% |
| **+20¢** | 16648 | 11597 | 5051 (101) | 1 | $-6415.29 | -6.1% |
| **+10¢ (15¢ stop)** | 36755 | 36696 | 59 (32) | 0 | $-13835.15 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 07:32 | +10 stop | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 10-23 07:31 | +10 stop | BTC | UP | 0.70 | 0.81 | 0.84 |
| 10-23 07:31 | +20 | BTC | UP | 0.70 | 0.91 | 1.89 |
| 10-23 07:31 | +15 | BTC | UP | 0.70 | 0.86 | 1.36 |
| 10-23 07:31 | +10 | BTC | UP | 0.70 | 0.81 | 0.84 |
| 10-23 07:31 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
| 10-23 07:31 | +10 stop | ZEC | DOWN | 0.58 | 0.33 | -2.84 |
| 10-23 07:31 | +20 | ZEC | DOWN | 0.58 | open |  |
| 10-23 07:31 | +15 | ZEC | DOWN | 0.58 | open |  |
| 10-23 07:31 | +10 | ZEC | DOWN | 0.58 | open |  |
| 10-23 07:31 | +5 | ZEC | DOWN | 0.58 | open |  |
| 10-23 07:25 | +10 stop | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 10-23 07:24 | +5 | HYPE | DOWN | 0.67 | 0.84 | 1.44 |
| 10-23 07:22 | +10 stop | HYPE | DOWN | 0.70 | 0.84 | 1.18 |
| 10-23 07:22 | +20 | HYPE | DOWN | 0.69 | 0.94 | 2.27 |
| 10-23 07:22 | +10 | HYPE | DOWN | 0.69 | 0.84 | 1.24 |
| 10-23 07:22 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.30 |
| 10-23 07:21 | +10 stop | BNB | UP | 0.61 | 0.43 | -2.15 |
| 10-23 07:21 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-23 07:19 | +15 | BNB | DOWN | 0.68 | 0.86 | 1.55 |
| 10-23 07:18 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-23 07:18 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-23 07:18 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-23 07:18 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.76 |
| 10-23 07:18 | +15 | HYPE | DOWN | 0.70 | 0.85 | 1.29 |
| 10-23 07:18 | +10 | HYPE | DOWN | 0.70 | 0.80 | 0.76 |
| 10-23 07:18 | +10 stop | BNB | DOWN | 0.64 | 0.43 | -2.45 |
| 10-23 07:18 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 07:17 | +5 | HYPE | DOWN | 0.68 | 0.80 | 0.92 |
| 10-23 07:17 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-23 07:17 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 10-23 07:17 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.22 |
| 10-23 07:17 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 07:17 | +20 | SOL | DOWN | 0.64 | 0.84 | 1.73 |
| 10-23 07:17 | +15 | SOL | DOWN | 0.64 | 0.82 | 1.52 |
| 10-23 07:17 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 07:17 | +5 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 07:17 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-23 07:17 | +20 | DOGE | DOWN | 0.69 | 0.90 | 1.88 |
| 10-23 07:17 | +15 | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
