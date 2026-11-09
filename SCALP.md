# Range-Scalp Bot

*Updated Mon Nov 09 14:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53755 | 46887 | 6868 (86) | 2 | $-14715.87 | -4.3% |
| **+10¢** | 40155 | 32142 | 8013 (112) | 1 | $-13697.95 | -5.4% |
| **+15¢** | 33653 | 25017 | 8636 (143) | 1 | $-12473.34 | -5.9% |
| **+20¢** | 29951 | 20891 | 9060 (189) | 1 | $-10956.08 | -5.8% |
| **+10¢ (15¢ stop)** | 65484 | 65378 | 106 (63) | 1 | $-24229.23 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 14:06 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-09 14:06 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-09 14:06 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 11-09 14:06 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-09 14:05 | +5 | NEAR | DOWN | 0.57 | 0.65 | 0.47 |
| 11-09 14:05 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 11-09 14:05 | +20 | SOL | DOWN | 0.69 | open |  |
| 11-09 14:05 | +15 | SOL | DOWN | 0.69 | 0.84 | 1.25 |
| 11-09 14:05 | +10 | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 11-09 14:05 | +5 | SOL | DOWN | 0.69 | 0.77 | 0.52 |
| 11-09 14:04 | +10 stop | NEAR | DOWN | 0.50 | 0.60 | 0.65 |
| 11-09 14:04 | +20 | NEAR | DOWN | 0.50 | 0.70 | 1.67 |
| 11-09 14:04 | +15 | NEAR | DOWN | 0.50 | 0.65 | 1.16 |
| 11-09 14:04 | +10 | NEAR | DOWN | 0.50 | 0.60 | 0.65 |
| 11-09 14:04 | +5 | NEAR | DOWN | 0.50 | 0.59 | 0.55 |
| 11-09 14:04 | +10 stop | HYPE | DOWN | 0.63 | 0.31 | -3.52 |
| 11-09 14:04 | +5 | HYPE | DOWN | 0.63 | open |  |
| 11-09 14:02 | +10 stop | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 11-09 14:02 | +20 | NEAR | DOWN | 0.66 | 0.89 | 2.07 |
| 11-09 14:02 | +15 | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 11-09 14:02 | +10 | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 11-09 14:02 | +5 | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 11-09 14:01 | +5 | HYPE | DOWN | 0.71 | 0.80 | 0.63 |
| 11-09 14:01 | +10 stop | SOL | DOWN | 0.67 | 0.80 | 1.05 |
| 11-09 14:01 | +20 | SOL | DOWN | 0.67 | 0.89 | 2.00 |
| 11-09 14:01 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.37 |
| 11-09 14:01 | +10 | SOL | DOWN | 0.67 | 0.80 | 1.05 |
| 11-09 14:01 | +5 | SOL | DOWN | 0.67 | 0.73 | 0.33 |
| 11-09 14:01 | +10 stop | HYPE | UP | 0.45 | 0.25 | -2.32 |
| 11-09 14:01 | +20 | HYPE | UP | 0.45 | 0.68 | 1.96 |
| 11-09 14:01 | +15 | HYPE | UP | 0.45 | 0.68 | 1.96 |
| 11-09 14:01 | +10 | HYPE | UP | 0.45 | 0.68 | 1.96 |
| 11-09 14:01 | +5 | HYPE | UP | 0.45 | 0.53 | 0.44 |
| 11-09 14:01 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-09 14:01 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-09 14:01 | +15 | ZEC | DOWN | 0.63 | 0.81 | 1.52 |
| 11-09 14:01 | +10 | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-09 14:01 | +5 | ZEC | DOWN | 0.63 | 0.72 | 0.58 |
| 11-09 13:46 | +10 stop | BNB | UP | 0.63 | 0.75 | 0.89 |
| 11-09 13:46 | +20 | BNB | UP | 0.63 | 0.84 | 1.83 |
