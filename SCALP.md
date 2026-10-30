# Range-Scalp Bot

*Updated Fri Oct 30 04:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40167 | 35087 | 5080 (51) | 0 | $-11013.34 | -4.4% |
| **+10¢** | 29930 | 24051 | 5879 (74) | 0 | $-9760.66 | -5.2% |
| **+15¢** | 25036 | 18709 | 6327 (101) | 0 | $-8748.59 | -5.6% |
| **+20¢** | 22216 | 15583 | 6633 (130) | 0 | $-7659.93 | -5.5% |
| **+10¢ (15¢ stop)** | 48987 | 48917 | 70 (37) | 0 | $-18489.12 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 04:01 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 04:01 | +20 | BNB | DOWN | 0.65 | 0.87 | 1.96 |
| 10-30 04:01 | +15 | BNB | DOWN | 0.65 | 0.87 | 1.96 |
| 10-30 04:01 | +10 | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 04:01 | +5 | BNB | DOWN | 0.65 | 0.74 | 0.60 |
| 10-30 04:01 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.93 |
| 10-30 04:01 | +20 | NEAR | DOWN | 0.64 | 0.87 | 2.08 |
| 10-30 04:01 | +15 | NEAR | DOWN | 0.64 | 0.83 | 1.67 |
| 10-30 04:01 | +10 | NEAR | DOWN | 0.64 | 0.76 | 0.94 |
| 10-30 04:01 | +5 | NEAR | DOWN | 0.64 | 0.72 | 0.52 |
| 10-30 04:01 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-30 04:01 | +20 | ZEC | DOWN | 0.69 | 0.90 | 1.88 |
| 10-30 04:01 | +15 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-30 04:01 | +10 | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-30 04:01 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-30 03:58 | +10 stop | NEAR | DOWN | 0.71 | 0.83 | 0.95 |
| 10-30 03:56 | +10 stop | HYPE | UP | 0.68 | 0.80 | 0.92 |
| 10-30 03:56 | +15 | HYPE | UP | 0.70 | no | -7.15 |
| 10-30 03:56 | +10 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-30 03:56 | +10 stop | NEAR | DOWN | 0.63 | 0.44 | -2.25 |
| 10-30 03:53 | +10 stop | BNB | UP | 0.62 | 0.81 | 1.62 |
| 10-30 03:53 | +10 stop | HYPE | UP | 0.70 | 0.38 | -3.52 |
| 10-30 03:53 | +5 | HYPE | UP | 0.70 | 0.76 | 0.32 |
| 10-30 03:51 | +10 stop | NEAR | DOWN | 0.65 | 0.48 | -2.04 |
| 10-30 03:51 | +5 | HYPE | UP | 0.58 | 0.64 | 0.25 |
| 10-30 03:51 | +10 stop | HYPE | UP | 0.54 | 0.64 | 0.65 |
| 10-30 03:51 | +15 | HYPE | UP | 0.54 | 0.71 | 1.37 |
| 10-30 03:51 | +5 | HYPE | UP | 0.54 | 0.61 | 0.35 |
| 10-30 03:50 | +10 stop | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-30 03:50 | +10 stop | BTC | UP | 0.65 | 0.78 | 1.01 |
| 10-30 03:50 | +10 stop | NEAR | UP | 0.52 | 0.35 | -2.04 |
| 10-30 03:50 | +15 | ZEC | DOWN | 0.53 | 0.76 | 1.99 |
| 10-30 03:49 | +10 stop | HYPE | DOWN | 0.53 | 0.36 | -2.05 |
| 10-30 03:49 | +10 | HYPE | DOWN | 0.54 | 0.67 | 0.92 |
| 10-30 03:48 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 10-30 03:48 | +10 | ETH | UP | 0.67 | 0.81 | 1.13 |
| 10-30 03:48 | +5 | ETH | UP | 0.68 | 0.81 | 1.03 |
| 10-30 03:48 | +10 stop | HYPE | DOWN | 0.45 | 0.59 | 1.05 |
| 10-30 03:48 | +10 | HYPE | DOWN | 0.44 | 0.59 | 1.14 |
| 10-30 03:47 | +10 stop | BNB | UP | 0.62 | 0.80 | 1.51 |
