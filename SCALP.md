# Range-Scalp Bot

*Updated Thu Oct 22 11:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28635 | 24952 | 3683 (39) | 3 | $-8237.24 | -4.6% |
| **+10¢** | 21490 | 17227 | 4263 (55) | 3 | $-7341.10 | -5.4% |
| **+15¢** | 17989 | 13404 | 4585 (78) | 3 | $-6567.45 | -5.8% |
| **+20¢** | 15915 | 11106 | 4809 (100) | 3 | $-5931.08 | -5.9% |
| **+10¢ (15¢ stop)** | 35130 | 35071 | 59 (32) | 1 | $-13157.07 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 11:07 | +10 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-22 11:07 | +10 stop | DOGE | UP | 0.65 | 0.81 | 1.33 |
| 10-22 11:07 | +10 stop | ZEC | DOWN | 0.59 | open |  |
| 10-22 11:06 | +10 stop | HYPE | UP | 0.65 | 0.76 | 0.81 |
| 10-22 11:06 | +5 | HYPE | UP | 0.67 | 0.73 | 0.33 |
| 10-22 11:05 | +10 stop | SOL | DOWN | 0.69 | 0.48 | -2.45 |
| 10-22 11:05 | +10 stop | DOGE | UP | 0.53 | 0.66 | 0.96 |
| 10-22 11:04 | +10 stop | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 10-22 11:04 | +15 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-22 11:04 | +10 | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 10-22 11:04 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 10-22 11:04 | +5 | SOL | DOWN | 0.70 | open |  |
| 10-22 11:03 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-22 11:03 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 10-22 11:03 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 10-22 11:03 | +5 | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 10-22 11:02 | +10 stop | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 10-22 11:02 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.50 |
| 10-22 11:02 | +10 stop | NEAR | DOWN | 0.57 | 0.69 | 0.87 |
| 10-22 11:01 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 10-22 11:01 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 10-22 11:01 | +15 | ETH | DOWN | 0.67 | 0.84 | 1.49 |
| 10-22 11:01 | +10 | ETH | DOWN | 0.67 | 0.81 | 1.18 |
| 10-22 11:01 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.45 |
| 10-22 11:01 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 11:01 | +20 | XRP | DOWN | 0.67 | 0.88 | 1.86 |
| 10-22 11:01 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 10-22 11:01 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 11:01 | +5 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 11:01 | +10 stop | ZEC | UP | 0.59 | 0.35 | -2.73 |
| 10-22 11:01 | +20 | ZEC | UP | 0.59 | open |  |
| 10-22 11:01 | +15 | ZEC | UP | 0.59 | open |  |
| 10-22 11:01 | +10 | ZEC | UP | 0.59 | open |  |
| 10-22 11:01 | +5 | ZEC | UP | 0.59 | open |  |
| 10-22 11:01 | +10 stop | HYPE | UP | 0.54 | 0.64 | 0.65 |
| 10-22 11:01 | +20 | HYPE | UP | 0.55 | 0.76 | 1.82 |
| 10-22 11:01 | +15 | HYPE | UP | 0.55 | 0.73 | 1.51 |
| 10-22 11:01 | +10 | HYPE | UP | 0.55 | 0.67 | 0.89 |
| 10-22 11:01 | +5 | HYPE | UP | 0.55 | 0.61 | 0.28 |
| 10-22 11:01 | +10 stop | NEAR | UP | 0.56 | 0.33 | -2.64 |
