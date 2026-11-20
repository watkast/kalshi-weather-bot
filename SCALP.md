# Range-Scalp Bot

*Updated Fri Nov 20 07:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66013 | 57612 | 8401 (124) | 1 | $-17780.55 | -4.3% |
| **+10¢** | 49296 | 39473 | 9823 (165) | 2 | $-16564.66 | -5.3% |
| **+15¢** | 41346 | 30750 | 10596 (212) | 3 | $-14925.53 | -5.8% |
| **+20¢** | 36811 | 25683 | 11128 (268) | 3 | $-13212.08 | -5.7% |
| **+10¢ (15¢ stop)** | 80385 | 80221 | 164 (98) | 0 | $-29631.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 07:07 | +10 stop | BNB | DOWN | 0.63 | 0.77 | 1.10 |
| 11-20 07:07 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-20 07:07 | +10 | BNB | DOWN | 0.63 | 0.77 | 1.08 |
| 11-20 07:07 | +5 | BNB | DOWN | 0.63 | 0.70 | 0.36 |
| 11-20 07:04 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 07:04 | +15 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-20 07:04 | +10 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 07:04 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.28 |
| 11-20 07:03 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 11-20 07:03 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 11-20 07:03 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.86 |
| 11-20 07:03 | +20 | BNB | DOWN | 0.66 | open |  |
| 11-20 07:03 | +15 | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 11-20 07:03 | +10 | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 11-20 07:03 | +5 | BNB | DOWN | 0.66 | 0.75 | 0.60 |
| 11-20 07:02 | +10 stop | NEAR | UP | 0.62 | 0.43 | -2.25 |
| 11-20 07:02 | +20 | NEAR | UP | 0.62 | open |  |
| 11-20 07:02 | +15 | NEAR | UP | 0.64 | open |  |
| 11-20 07:02 | +10 | NEAR | UP | 0.63 | open |  |
| 11-20 07:02 | +5 | NEAR | UP | 0.63 | open |  |
| 11-20 07:02 | +10 stop | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 11-20 07:02 | +20 | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-20 07:02 | +15 | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 11-20 07:02 | +10 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 11-20 07:02 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
| 11-20 07:02 | +5 | XRP | UP | 0.48 | 0.54 | 0.24 |
| 11-20 07:02 | +10 stop | XRP | UP | 0.58 | 0.41 | -2.05 |
| 11-20 07:02 | +20 | XRP | UP | 0.58 | open |  |
| 11-20 07:02 | +15 | XRP | UP | 0.58 | open |  |
| 11-20 07:02 | +10 | XRP | UP | 0.59 | open |  |
| 11-20 07:02 | +5 | XRP | UP | 0.56 | 0.61 | 0.15 |
| 11-20 07:01 | +10 stop | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 11-20 07:01 | +20 | HYPE | DOWN | 0.58 | 0.84 | 2.32 |
| 11-20 07:01 | +15 | HYPE | DOWN | 0.58 | 0.77 | 1.59 |
| 11-20 07:01 | +10 | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 11-20 07:01 | +5 | HYPE | DOWN | 0.58 | 0.64 | 0.25 |
| 11-20 07:01 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-20 07:01 | +20 | BTC | DOWN | 0.61 | 0.82 | 1.82 |
| 11-20 07:01 | +15 | BTC | DOWN | 0.62 | 0.77 | 1.20 |
| 11-20 07:01 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
