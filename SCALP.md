# Range-Scalp Bot

*Updated Sun Nov 08 00:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51713 | 45092 | 6621 (80) | 0 | $-14336.82 | -4.4% |
| **+10¢** | 38591 | 30871 | 7720 (106) | 0 | $-13336.87 | -5.5% |
| **+15¢** | 32315 | 23995 | 8320 (135) | 0 | $-12235.29 | -6.0% |
| **+20¢** | 28745 | 20022 | 8723 (180) | 0 | $-10782.61 | -6.0% |
| **+10¢ (15¢ stop)** | 62962 | 62859 | 103 (61) | 0 | $-23298.65 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 00:09 | +10 stop | BNB | UP | 0.61 | 0.95 | 3.21 |
| 11-08 00:06 | +10 stop | XRP | DOWN | 0.69 | 0.51 | -2.13 |
| 11-08 00:06 | +20 | XRP | DOWN | 0.69 | 0.93 | 2.13 |
| 11-08 00:06 | +15 | XRP | DOWN | 0.69 | 0.88 | 1.62 |
| 11-08 00:06 | +10 | XRP | DOWN | 0.69 | 0.88 | 1.67 |
| 11-08 00:06 | +5 | XRP | DOWN | 0.69 | 0.76 | 0.42 |
| 11-08 00:04 | +10 stop | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-08 00:03 | +10 stop | NEAR | UP | 0.44 | 0.57 | 0.94 |
| 11-08 00:03 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.98 |
| 11-08 00:03 | +20 | ZEC | DOWN | 0.68 | 0.90 | 2.03 |
| 11-08 00:03 | +15 | ZEC | DOWN | 0.63 | 0.81 | 1.50 |
| 11-08 00:03 | +10 | ZEC | DOWN | 0.63 | 0.74 | 0.77 |
| 11-08 00:03 | +5 | ZEC | DOWN | 0.63 | 0.74 | 0.77 |
| 11-08 00:02 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 11-08 00:02 | +20 | SOL | DOWN | 0.63 | 0.83 | 1.73 |
| 11-08 00:02 | +15 | SOL | DOWN | 0.63 | 0.81 | 1.52 |
| 11-08 00:02 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 11-08 00:02 | +5 | SOL | DOWN | 0.63 | 0.72 | 0.58 |
| 11-08 00:02 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 11-08 00:02 | +5 | HYPE | DOWN | 0.60 | 0.69 | 0.53 |
| 11-08 00:02 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-08 00:02 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-08 00:02 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 11-08 00:02 | +5 | HYPE | DOWN | 0.59 | 0.64 | 0.16 |
| 11-08 00:02 | +10 stop | BNB | UP | 0.62 | 0.45 | -2.05 |
| 11-08 00:02 | +20 | BNB | UP | 0.62 | 0.95 | 3.11 |
| 11-08 00:02 | +15 | BNB | UP | 0.64 | 0.95 | 2.96 |
| 11-08 00:02 | +10 | BNB | UP | 0.64 | 0.95 | 2.96 |
| 11-08 00:02 | +5 | BNB | UP | 0.64 | 0.70 | 0.33 |
| 11-08 00:02 | +10 stop | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-08 00:02 | +20 | DOGE | DOWN | 0.70 | 0.94 | 2.15 |
| 11-08 00:02 | +15 | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 11-08 00:02 | +10 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-08 00:02 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-08 00:01 | +10 stop | XRP | DOWN | 0.54 | 0.67 | 0.96 |
| 11-08 00:01 | +20 | XRP | DOWN | 0.54 | 0.76 | 1.89 |
| 11-08 00:01 | +15 | XRP | DOWN | 0.54 | 0.76 | 1.89 |
| 11-08 00:01 | +10 | XRP | DOWN | 0.54 | 0.67 | 0.96 |
| 11-08 00:01 | +5 | XRP | DOWN | 0.54 | 0.60 | 0.25 |
| 11-08 00:01 | +10 stop | NEAR | DOWN | 0.57 | 0.41 | -1.95 |
