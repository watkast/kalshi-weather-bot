# Range-Scalp Bot

*Updated Thu Oct 22 01:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28015 | 24406 | 3609 (39) | 5 | $-8079.90 | -4.6% |
| **+10¢** | 21043 | 16875 | 4168 (55) | 7 | $-7124.09 | -5.4% |
| **+15¢** | 17628 | 13143 | 4485 (78) | 7 | $-6351.60 | -5.7% |
| **+20¢** | 15602 | 10902 | 4700 (98) | 8 | $-5693.21 | -5.8% |
| **+10¢ (15¢ stop)** | 34410 | 34351 | 59 (32) | 2 | $-12866.39 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 01:11 | +5 | BTC | UP | 0.55 | 0.64 | 0.55 |
| 10-22 01:11 | +10 stop | BNB | DOWN | 0.60 | open |  |
| 10-22 01:11 | +10 | BNB | DOWN | 0.60 | open |  |
| 10-22 01:11 | +5 | BNB | DOWN | 0.60 | open |  |
| 10-22 01:10 | +10 stop | BTC | DOWN | 0.53 | 0.35 | -2.14 |
| 10-22 01:10 | +5 | BTC | DOWN | 0.53 | 0.58 | 0.14 |
| 10-22 01:10 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.79 |
| 10-22 01:09 | +10 stop | HYPE | UP | 0.63 | 0.84 | 1.83 |
| 10-22 01:09 | +10 stop | NEAR | UP | 0.66 | 0.80 | 1.12 |
| 10-22 01:09 | +10 stop | BTC | DOWN | 0.65 | 0.49 | -1.94 |
| 10-22 01:08 | +5 | XRP | UP | 0.61 | 0.70 | 0.58 |
| 10-22 01:08 | +10 stop | SOL | UP | 0.64 | 0.40 | -2.74 |
| 10-22 01:08 | +10 stop | BNB | DOWN | 0.66 | 0.78 | 0.91 |
| 10-22 01:08 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-22 01:08 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-22 01:08 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 01:08 | +5 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 01:08 | +10 stop | XRP | UP | 0.64 | open |  |
| 10-22 01:08 | +5 | XRP | UP | 0.64 | 0.69 | 0.18 |
| 10-22 01:08 | +10 stop | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 10-22 01:08 | +20 | ETH | DOWN | 0.63 | open |  |
| 10-22 01:08 | +15 | ETH | DOWN | 0.64 | 0.82 | 1.52 |
| 10-22 01:08 | +10 | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 10-22 01:08 | +5 | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 10-22 01:08 | +10 stop | BTC | DOWN | 0.65 | 0.50 | -1.84 |
| 10-22 01:08 | +20 | BTC | DOWN | 0.65 | open |  |
| 10-22 01:08 | +15 | BTC | DOWN | 0.65 | open |  |
| 10-22 01:08 | +10 | BTC | DOWN | 0.65 | open |  |
| 10-22 01:08 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-22 01:07 | +10 stop | XRP | UP | 0.48 | 0.64 | 1.25 |
| 10-22 01:07 | +5 | XRP | UP | 0.53 | 0.64 | 0.75 |
| 10-22 01:06 | +10 stop | SOL | DOWN | 0.59 | 0.38 | -2.44 |
| 10-22 01:06 | +10 | SOL | DOWN | 0.59 | open |  |
| 10-22 01:06 | +5 | SOL | DOWN | 0.59 | open |  |
| 10-22 01:06 | +10 stop | ZEC | UP | 0.63 | 0.80 | 1.41 |
| 10-22 01:06 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.84 |
| 10-22 01:06 | +10 stop | HYPE | DOWN | 0.58 | 0.33 | -2.84 |
| 10-22 01:06 | +15 | HYPE | DOWN | 0.58 | open |  |
| 10-22 01:06 | +10 | HYPE | DOWN | 0.58 | open |  |
| 10-22 01:06 | +5 | HYPE | DOWN | 0.58 | open |  |
